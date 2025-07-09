# PRODIGY_DS_05
US Traffic Accident Analysis (2016–2023)
This project analyzes over 7 million US traffic accident records (2016–2023) to identify patterns based on time of day, weather and road conditions. It visualizes accident hotspots using interactive maps and explores contributing factors with plots, offering insights into traffic safety trends.

## Dataset
- Source: Kaggle ([Link](https://www.kaggle.com/datasets/sobhanmoosavi/us-accidents))
- File Used: US_Accidents_March23.csv

## Technologies Used
- Python
- Pandas
- Matplotlib and Seaborn
- Folium

## How to Run the Project
1. Clone the repository or download this folder
2. Install required libraries:
   `bash
   pip install pandas matplotlib seaborn folium
3. Download the dataset file US_Accidents_March23.csv in your project folder
4. Run the main.py script:
   python main.py
5. View all plots in the visuals/ folder
   Open the map file in a browser: visuals/accident_hotspots_map.html

## Visual Outputs (All Saved to visuals/ Folder)
- accidents_by_hour.png : Number of accidents by hour of day
- top_weather_conditions.png : Top 10 weather conditions in accidents
- traffic_signal_impact.png : Effect of traffic signal presence
- severity_weather_correlation.png : Correlation heatmap (severity vs weather factors)
- accident_hotspots_map.html : Interactive map of accident hotspots

# Note
- The dataset is very large (3GB).
  For slower systems, use: "df = pd.read_csv('US_Accidents_March23.csv', nrows=500000)"
- As the dataset file exceeds GitHub's 100 MB upload limit, it cannot be uploaded directly to the repository.