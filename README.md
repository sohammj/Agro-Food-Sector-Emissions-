CO₂ Emissions Forecasting in the Agro-Food Sector  

Project Overview  
This project analyzes and forecasts CO₂ emissions and temperature trends in the agro-food sector, a significant contributor to global greenhouse gas (GHG) emissions. Using advanced statistical methods like Winter's Method (Triple Exponential Smoothing), it provides actionable insights into emission trends, enabling policymakers to develop sustainable strategies to mitigate climate change.  

An interactive Tableau dashboard complements this analysis, visualizing emissions and temperature trends dynamically, along with key metrics like emissions by country and temperature changes over time.  

Key Features  
- Advanced Forecasting Models: Applied both additive and multiplicative forms of Winter's Method to account for seasonal and trend components.  
- Interactive Dashboard: Visualizes CO₂ emissions, temperature trends, and country-specific metrics, aiding comprehensive policy planning.  
- High-Accuracy Results: Models validated with Mean Absolute Error (MAE) and Mean Squared Error (MSE) for precision.  
- Environmental Impact: Highlights the importance of sustainable agricultural practices to combat climate change.  

Technical Highlights  
- Forecasting Models:  
  - Additive Winter's Method: For stable seasonal fluctuations.  
  - Multiplicative Winter's Method: For seasonality proportional to trends.  
- Dataset: Processed from FAO and IPCC sources, focusing on:  
  - CO₂ emissions  
  - Agricultural land use, livestock, and fertilizer application  
  - Average temperatures  
- Technologies:  
  - Python for data analysis and visualization  
  - Tableau for interactive dashboards  

Visualization  
Example: Interactive Dashboard   
Explore CO₂ emissions trends, global temperature changes, and country-specific metrics interactively.  

How to Use  
1. Code:  
   - Install dependencies:  
     pip install -r requirements.txt  
   - Run the forecasting scripts in the `code/` directory to generate predictions.  
2. Dataset:  
   - The dataset is included in the `dataset/` directory. Ensure compatibility with scripts for preprocessing.  
3. Dashboard:  
   - Open the Tableau `.twbx` file in Tableau Desktop to explore visualizations.  

Findings  
- Emission Trends: A steady rise in CO₂ emissions is projected through 2030 if current agricultural practices remain unchanged.  
- Temperature Trends: Average temperatures are forecasted to rise significantly, aligning with global climate change studies.  
- Policy Implications: Immediate interventions are required to implement sustainable agricultural practices and reduce emissions.  

Future Work  
- Incorporate ARIMA and machine learning models to enhance forecasting precision.  
- Expand dataset to include additional environmental and socio-economic variables.  

Acknowledgments  
- Faculty Advisors: Dr. Khinal Parmar, Dr. Mahesh Mali  
- Data Sources: Kaggle, FAO, IPCC  
