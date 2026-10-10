"use strict";

const $ = (id) => document.getElementById(id);
let ready = false;
const percent = (n) => Number.isFinite(Number(n)) ? `${(Number(n) * 100).toFixed(2)}%` : "—";
const fixed4 = (n) => Number.isFinite(Number(n)) ? Number(n).toFixed(4) : "—";

async function getJSON(url, init) {
  const response = await fetch(url, init);
  const data = await response.json();
  if (!response.ok) throw new Error(data.error || `HTTP ${response.status}`);
  return data;
}

async function initialize() {
  try {
    const status = await getJSON('/api/status');
    ready = status.ready;
    const statusNode = $('model-status');
    statusNode.classList.toggle('status-ready', ready);
    statusNode.classList.toggle('status-missing', !ready);
    statusNode.querySelector('span:last-child').textContent = ready ? 'Model ready' : 'Model not exported';
    const button = $('predict-btn');
    button.disabled = !ready;
    if (!ready) showError(status.error || 'Export the model before making predictions.');
  } catch (error) {
    showError(`Cannot connect to the local prediction server: ${error.message}`);
    $('model-status').querySelector('span:last-child').textContent = 'Server unavailable';
    $('predict-btn').disabled = true;
  }
  try {
    const data = await getJSON('/api/metrics');
    $('metric-accuracy').textContent = percent(data.Accuracy);
    $('metric-precision').textContent = percent(data.Precision);
    $('metric-recall').textContent = percent(data.Recall);
    $('metric-f1').textContent = fixed4(data['F1-score']);
    $('metric-roc-auc').textContent = fixed4(data['ROC-AUC']);
    $('metric-pr-auc').textContent = fixed4(data['PR-AUC']);
    $('hero-recall').textContent = percent(data.Recall);
    $('hero-prauc').textContent = fixed4(data['PR-AUC']);
  } catch (error) {
    // This does not block prediction: the model can work without its metrics CSV.
  }
}

function showError(message) {
  const element = $('result-error');
  element.textContent = message;
  element.hidden = false;
}

function clearFeedback() {
  $('result-error').hidden = true;
  $('result-error').textContent = '';
  $('result-warnings').hidden = true;
  $('result-warnings').replaceChildren();
}

$('booking-form').addEventListener('submit', async (event) => {
  event.preventDefault();
  clearFeedback();
  if (!ready) {
    showError('The trained model is not available. Run the export command, then restart this server.');
    return;
  }
  const form = event.currentTarget;
  if (!form.reportValidity()) return;
  const payload = Object.fromEntries(new FormData(form));
  const button = $('predict-btn');
  button.disabled = true;
  const oldHTML = button.innerHTML;
  button.textContent = 'Calculating risk...';
  try {
    const result = await getJSON('/api/predict', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload),
    });
    const pct = result.probability * 100;
    const ring = $('risk-ring');
    ring.style.setProperty('--score', `${pct}%`);
    ring.style.setProperty('--risk-color', result.flagged ? '#e08b5b' : '#159c89');
    $('risk-score').textContent = `${pct.toFixed(1)}%`;
    $('risk-title').textContent = result.label;
    $('risk-title').classList.toggle('high-risk', result.flagged);
    $('risk-message').textContent = result.flagged
      ? "Elevated risk: Consider appropriate reservation follow-up and human review."
      : "Below alert threshold: Continue normal reservation management.";
    const warningBox = $('result-warnings');
    if (result.warnings?.length) {
      for (const warning of result.warnings) {
        const p = document.createElement('p');
        p.textContent = '⚠ ' + warning;
        warningBox.append(p);
      }
      warningBox.hidden = false;
    }
    if (matchMedia('(max-width: 900px)').matches) {
      $('result-panel').scrollIntoView({behavior:'smooth', block:'center'});
    }
  } catch (error) {
    showError(error.message);
  } finally {
    button.disabled = false;
    button.innerHTML = oldHTML;
  }
});

initialize();
