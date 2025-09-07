import argparse
import numpy as np
import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing
import google.generativeai as genai

# -------------------
# Configure Gemini API
# -------------------
genai.configure(api_key="AIzaSyC2EVCSgC-DRWVunkKi7Ro0J1upoN3UglE")  # Replace with your Gemini API key
model = genai.GenerativeModel("gemini-1.5-flash")

# -------------------
# Helper: Usage Level
# -------------------
def usage_level(consumption):
    avg_recent = np.mean(consumption[-3:])
    if avg_recent > 10:  # kWh
        return "High Energy Usage 🔴"
    elif avg_recent > 5:
        return "Moderate Energy Usage 🟠"
    else:
        return "Low Energy Usage 🟢"

# -------------------
# Forecast Function
# -------------------
def energy_forecast(usage_history):
    if len(usage_history) < 5:
        print("❌ Error: Need at least 5 data points for forecasting.")
        return

    series = pd.Series(usage_history)

    # Holt-Winters forecasting
    model_hw = ExponentialSmoothing(series, trend="add", seasonal=None)
    model_fit = model_hw.fit()
    forecast_values = model_fit.forecast(steps=5)

    trend = "increasing 📈" if np.mean(forecast_values) > np.mean(usage_history) else "decreasing 📉"
    level = usage_level(usage_history)

    # AI Prompt
    prompt = f"""
    You are an AI Smart Home Energy Advisor.
    Given the home energy usage history (kWh): {usage_history}
    Forecasted next 5 consumption values (kWh): {list(forecast_values)}
    Trend: {trend}
    Usage Level: {level}

    Provide:
    1. Tips to optimize home energy usage and reduce waste.
    2. Short explanation of why these tips are effective.
    3. Suggestions for potential cost savings.
    """

    response = model.generate_content(prompt)
    ai_text = response.text if response else "❌ No AI response"

    # Split AI output
    parts = ai_text.split("\n", 1)
    recommendation = parts[0].strip() if parts else "Not generated"
    explanation = parts[1].strip() if len(parts) > 1 else ai_text

    # Display
    print("\n🏠 Smart Home Energy Forecast & AI Recommendations")
    print("-" * 60)
    print(f"Next 5 Forecasted Consumption (kWh): {list(np.round(forecast_values, 2))}")
    print(f"Trend                               : {trend}")
    print(f"Usage Level                         : {level}\n")
    print("🤖 AI Recommendations:")
    print(recommendation)
    print("\nAI Explanation:")
    print(explanation)

# -------------------
# CLI Setup
# -------------------
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="🏠 Smart Home Energy AI (Terminal Version)")
    parser.add_argument("--usage", type=str, help="Space-separated home energy usage (kWh, at least 5 values)")

    args = parser.parse_args()

    if args.usage:
        raw_input = args.usage
    else:
        print("Enter home energy usage in kWh separated by spaces (at least 5 values):")
        raw_input = input()

    usage_history = [float(x) for x in raw_input.strip().split()]
    energy_forecast(usage_history)
