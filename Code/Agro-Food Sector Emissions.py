#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 21:01:42 2024

@author: soham
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def winters(data, alpha, beta, gamma, seasonlength, fp):
    level = data[0]
    trend = data[1] - data[0]
    seasonals = [data[i] - data[0] for i in range(seasonlength)]
    forecast = []
    
    for t in range(len(data)):
        if t >= seasonlength:
            lastlevel = level
            lasttrend = trend
            level = alpha * (data[t] - seasonals[t % seasonlength]) + (1 - alpha) * (lastlevel + lasttrend)
            trend = beta * (level - lastlevel) + (1 - beta) * lasttrend
            seasonals[t % seasonlength] = gamma * (data[t] - level) + (1 - gamma) * seasonals[t % seasonlength]
        forecast.append(level + trend + seasonals[t % seasonlength])
    
    # future Forecats
    for t in range(fp):
        last_level = level
        last_trend = trend
        level = alpha * (level + trend) + (1 - alpha) * (last_level + last_trend)
        trend = beta * (level - last_level) + (1 - beta) * last_trend
        seasonals.append(seasonals[-seasonlength])  
        forecast.append(level + trend + seasonals[-seasonlength])
    
    return forecast

def winters_MULTI(data, alpha, beta, gamma, seasonlength, fp):
    level = data[0]
    trend = data[1] / data[0]  # Trend is now multiplicative
    seasonals = [data[i] / data[0] for i in range(seasonlength)]  # Seasonal factors are multiplicative
    forecast = []
    
    for t in range(len(data)):
        if t >= seasonlength:
            lastlevel = level
            lasttrend = trend
            level = alpha * (data[t] / seasonals[t % seasonlength]) + (1 - alpha) * (lastlevel * lasttrend)
            trend = beta * (level / lastlevel) + (1 - beta) * lasttrend
            seasonals[t % seasonlength] = gamma * (data[t] / level) + (1 - gamma) * seasonals[t % seasonlength]
        forecast.append((level + trend) * seasonals[t % seasonlength])
    
    # Future forecasts
    for t in range(fp):
        last_level = level
        last_trend = trend
        level = alpha * (level * trend) + (1 - alpha) * (last_level * last_trend)
        trend = beta * (level / last_level) + (1 - beta) * last_trend
        seasonals.append(seasonals[-seasonlength])  
        forecast.append((level + trend) * seasonals[-seasonlength])
    
    return forecast

def plot_forecast(years, actualdata, forecastdata, labelactual, labelforecast, title, ylabel, forecastyears):
    plt.figure(figsize=(12, 6))
    
    futureyears = np.arange(years[-1] + 1, years[-1] + 1 + forecastyears)
    extended_years = np.concatenate([years, futureyears])
    
    # Plot actual and forecast data
    plt.plot(years, actualdata, label=labelactual, color='blue', marker='o', linestyle='-')
    plt.plot(extended_years, forecastdata, label=labelforecast, color='red', linestyle='--')
    
    plt.title(title)
    plt.xlabel("Year")
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def calculate_accuracy_metrics(actual, forecast):
    mae = np.mean(np.abs(actual - forecast[:len(actual)]))
    mse = np.mean((actual - forecast[:len(actual)])**2)
    print(f"Mean Absolute Error (MAE): {mae}")
    print(f"Mean Squared Error (MSE): {mse}")

def main():
    df = pd.read_csv('/Users/soham/Downloads/Agrofood_co2_emission 3.csv')
    
    df['Year'] = pd.to_numeric(df['Year'], errors='coerce')
    numericcols = df.select_dtypes(include=[np.number])  
    df_aggregated = numericcols.groupby('Year').mean().reset_index()
    years = df_aggregated['Year'].values
    
    total_emission = df_aggregated.get('total_emission', np.array([])).values
    at = df_aggregated.get('Average Temperature °C', np.array([])).values
    
    season_length = 12
    alpha1, beta1, gamma1 = 0.9, 0.03, 0.9 
    alpha,beta,gamma=0.9,0.1,0.9
    forecastyears = 10

    forecast_total_emission = winters_MULTI(total_emission, alpha1, beta1, gamma1, season_length, forecastyears)
    ft = winters(at, alpha, beta, gamma, season_length, forecastyears)
    
   
    plot_forecast(years, total_emission, forecast_total_emission, "Actual Emissions", "Forecasted Emissions", "CO2 Emissions Forecast", "Emissions (kt)", forecastyears)

   
    plot_forecast(years, at, ft, "Actual Temperature", "Forecasted Temperature", "Average Temperature Forecast", "Temperature (°C)", forecastyears)

    
    print("Accuracy for Total Emissions:")
    calculate_accuracy_metrics(total_emission, forecast_total_emission)
    
    print("\nAccuracy for Average Temperature:")
    calculate_accuracy_metrics(at, ft)

if __name__ == "__main__":
    main()
