# supply-chain-analytics-app
SupplyChainX is a full-stack analytics platform for procurement pros. Built with React, Node.js, and PostgreSQL, it features an interactive P2P learning module, live supplier performance charts via Recharts, and a risk simulator for warehouse capacity. It bridges the gap between supply chain domain expertise and modern data science.
📦 SupplyChainX: A Full-Stack Analytics & Learning Ecosystem
🌟 Executive Summary
SupplyChainX is a sophisticated, full-stack web application designed to solve the "visibility gap" in modern procurement and logistics operations. While many supply chain professionals rely on static spreadsheets, this platform demonstrates the power of a custom React-Node-PostgreSQL stack to provide real-time, interactive insights.

The project was born from a specific professional need: to simplify the complex Procure-to-Pay (P2P) lifecycle for junior buyers while giving senior management a high-level view of supplier risk and warehouse performance. By combining educational modules with live data visualization, SupplyChainX serves as both a training tool and a functional analytics dashboard.

🧠 Core Modules & Functionality
1. Interactive P2P Learning "Slides"
The application features a dedicated learning module that visualizes the procurement journey. Unlike a static PDF, this module uses React State Management to let users "click through" the stages of a Purchase Request, RFQ, and Purchase Order. Each slide contains:

Process Definitions: Clear, concise explanations of the technical steps.

Operational Checklists: Actionable items (e.g., "Verify Budget," "Technical Specs").

Professional Pro-Tips: Real-world advice on negotiation and compliance based on industry best practices.

2. Live Supplier Performance Dashboard
To demonstrate data proficiency, the app integrates a PostgreSQL relational database. Using the Recharts library, the dashboard pulls live metrics to compare:

Lead Time vs. Unit Cost: Identifying the "Sweet Spot" between speed and price.

Quality Scores: Tracking vendor reliability over time.

Spend Analytics: Aggregating total procurement costs for executive review.

3. Real-World Risk Simulation
Supply chain is about managing the unexpected. The platform includes a Scenario Simulator where users encounter challenges like supplier delays or sudden warehouse capacity spikes. Users interact with a "Warehouse Capacity" slider (0-100%) and decision buttons that trigger logic-based feedback, teaching them how to optimize safety stock and mitigate risk during disruptions.

🛠️ Technical Architecture
Frontend: Developed using React.js for a dynamic, single-page application experience.

Backend API: A RESTful API built with Node.js and Express.js to handle secure data transmission.

Database: A structured PostgreSQL schema designed for complex relational queries.

Connectivity: Seamless integration between the frontend and backend using CORS and Fetch API, ensuring the internet-connected dashboard stays updated with the latest SQL data.

🎯 Professional Impact
This project bridges the gap between Supply Chain Domain Expertise and Full-Stack Development. It proves a mastery of SQL for data management, JavaScript for interactive UI, and architectural thinking for deploying professional-grade IT solutions in the logistics sector.
