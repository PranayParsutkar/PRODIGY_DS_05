import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium
import os

df = pd.read_csv('US_Accidents_March23.csv')
df = df[['Start_Time', 'Severity', 'Start_Lat', 'Start_Lng', 
         'Weather_Condition', 'Temperature(F)', 'Humidity(%)', 
         'Visibility(mi)', 'Wind_Speed(mph)', 'Traffic_Signal']].dropna()
df['Start_Time'] = pd.to_datetime(df['Start_Time'], errors='coerce', format='mixed')
df['Hour'] = df['Start_Time'].dt.hour
df['Weekday'] = df['Start_Time'].dt.day_name()

plt.figure(figsize=(10, 4))
sns.countplot(x='Hour', data=df)
plt.title('Accidents by Hour of Day')
plt.xlabel('Hour'); plt.ylabel('Number of Accidents')
plt.tight_layout()
plt.savefig('visuals/accidents_by_hour.png')  
plt.show()

plt.figure(figsize=(12, 4))
df['Weather_Condition'].value_counts().head(10).plot(kind='bar', color='blue')
plt.title('Top 10 Weather Conditions During Accidents')
plt.xlabel('Weather Condition'); plt.ylabel('Count')
plt.tight_layout()
plt.savefig('visuals/top_weather_conditions.png')
plt.show()

plt.figure(figsize=(5, 4))
sns.countplot(x='Traffic_Signal', data=df)
plt.title('Accidents with Traffic Signal Present')
plt.xlabel('Traffic Signal Present?'); plt.ylabel('Accident Count')
plt.tight_layout()
plt.savefig('visuals/traffic_signal_impact.png')
plt.show()

map_sample = df[['Start_Lat', 'Start_Lng']].sample(1000)
m = folium.Map(location=[39.5, -98.35], zoom_start=5)
for i, row in map_sample.iterrows():
    folium.CircleMarker(
        location=[row['Start_Lat'], row['Start_Lng']],
        radius=1,
        color='crimson',
        fill=True
    ).add_to(m)
m.save('visuals/accident_hotspots_map.html')

plt.figure(figsize=(6, 5))
corr = df[['Severity', 'Temperature(F)', 'Humidity(%)', 
           'Visibility(mi)', 'Wind_Speed(mph)']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Between Severity and Weather Factors')
plt.tight_layout()
plt.savefig('visuals/severity_weather_correlation.png')
plt.show()