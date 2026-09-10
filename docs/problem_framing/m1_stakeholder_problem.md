# Member 1 — Stakeholder and Business Problem

**Owner:** IT24101668

## Stakeholder

**Hotel Revenue Management and Operations Teams**

The primary stakeholders are revenue managers, hotel operations managers, and booking systems administrators who are responsible for:
- Maximizing revenue and occupancy rates
- Managing staff scheduling and resource allocation
- Ensuring guest satisfaction and retention
- Optimizing inventory and pricing strategies

Secondary stakeholders include the executive leadership team who depend on revenue forecasts and the booking platform that manages customer reservations.

## Business Problem

Hotel booking cancellations represent a significant operational and financial challenge. When customers cancel reservations, it creates:

1. **Revenue Loss** — Rooms become unoccupied without advance notice, reducing the ability to resell at optimal rates or redirect resources
2. **Inventory Planning Inefficiency** — Operations teams struggle to predict staffing needs, housekeeping schedules, and supply chain requirements
3. **Overbooking Risk** — Without accurate cancellation forecasts, hotels must choose between accepting overbooking risks or maintaining excess inventory
4. **Customer Experience Impact** — Reactive measures to cancellations can result in poor service quality or inability to accommodate walk-in guests

**Core Problem:** Hotel revenue and operations teams lack the ability to proactively identify high-risk bookings, resulting in reactive strategies and suboptimal resource allocation.

## Why the Problem Matters

The financial and operational impact is substantial:

- **Revenue Impact:** In the tourism and hospitality sector, last-minute cancellations can account for 20-40% of bookings, directly reducing revenue
- **Competitive Pressure:** Hotels that can better predict and manage cancellations gain a competitive advantage in pricing and resource optimization
- **Guest Satisfaction:** Poor resource planning due to unpredicted cancellations leads to downgrades, service delays, or unavailable amenities
- **Operational Efficiency:** Accurate cancellation predictions enable data-driven decisions for staffing, maintenance scheduling, and inventory management
- **Strategic Growth:** Understanding cancellation patterns supports better pricing strategies, customer segmentation, and market positioning

Without addressing this problem, hotels operate reactively with inflexible pricing, inefficient scheduling, and reduced profitability.

## Evidence / Reasoning

1. **Industry Context:** The Hotel Booking Demand dataset contains real-world booking patterns that reflect actual cancellation behaviors. Cancellation rates are non-trivial and vary significantly based on booking characteristics.

2. **Data Availability:** The dataset includes rich features (booking lead time, guest type, arrival month, special requests, etc.) that logically relate to cancellation likelihood, suggesting predictive patterns exist.

3. **Business Logic:** Different booking profiles have demonstrably different cancellation behaviors:
   - Last-minute bookings vs. advance bookings
   - Bookings with special requests vs. standard bookings
   - Weekend vs. weekday arrivals
   - Different guest types and origin markets

4. **ML Feasibility:** A binary classification model can classify bookings as "high cancellation risk" or "low cancellation risk," enabling actionable segmentation of the booking portfolio.

5. **Practical Application:** Revenue teams can use predictions to:
   - Apply dynamic cancellation policies based on risk
   - Adjust overbooking rates strategically
   - Allocate resources more efficiently
   - Target retention efforts on high-risk bookings

This problem is both impactful and solvable through machine learning approaches.
