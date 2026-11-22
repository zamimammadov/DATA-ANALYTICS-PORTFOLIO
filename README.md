# Data analytics portfolio

Power BI reports, SQL reconciliations and Python analyses by Zamin Mammadov. Each project includes its data sources, metric definitions and instructions for inspecting or reproducing the results.

## Hotel revenue and occupancy

AtliQ Grands recorded **134,590 room bookings against 232,576 available check-in slots** in the supplied data, or **57.87% booked occupancy**. This measure includes bookings that were later cancelled. The report separates booking demand, realised revenue and cancellations so a reader can investigate the difference. [Report, presentation and metric checks](Hospitality%20Revenue%20Analytics%20Dashboard%20%28Power%20BI%29%20%E2%80%94%20AtliQ%20Grands/README.md)

![AtliQ Grands dashboard showing revenue, occupancy and booking performance](Hospitality%20Revenue%20Analytics%20Dashboard%20%28Power%20BI%29%20%E2%80%94%20AtliQ%20Grands/preview/dashboard.png)

## Explore the projects

| Project | Question | Tools |
|---|---|---|
| [Sales reconciliation](PowerBI/Sales/README.md) | Do the database transactions reproduce the Power BI revenue figures, and how does cleaning the currency codes change the answer? | MySQL, Power BI |
| [Attendance patterns](PowerBI/HR%20Analytics/README.md) | How do presence, remote work and sick leave vary over time, and which days belong in each denominator? | Excel, Power BI |
| [T20 World Cup scorecards](CricketAnalysis/README.md) | Who led the tournament in runs and wickets after matching player names and converting overs to legal balls? | Python, pandas |
| [Falcon 9 landing prediction](coursework/Predicting-SpaceX-Falcon-9-First-Stage-Landing-Success/README.md) | How well do models trained on earlier launches predict later landings? | Python, scikit-learn, Dash, SQL |
| [NextonNetflix](coursework/NextonNetflix/README.md) | Which films have similar cast, director and genre information, and how does a local classifier label reviews? | Python, Flask, scikit-learn |
