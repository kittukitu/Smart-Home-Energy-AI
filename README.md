# 🏠 Smart Home Energy AI

An **AI-powered smart home energy advisor** that forecasts electricity consumption and provides **personalized recommendations** for saving energy and reducing costs.  
It combines **Holt-Winters time series forecasting** with **Gemini AI** to generate actionable tips.

---

## 🚀 Features
- Forecasts next **5 periods of energy consumption (kWh)**.
- Detects **usage trends** (increasing/decreasing).
- Categorizes energy consumption into:
  - 🔴 High Usage  
  - 🟠 Moderate Usage  
  - 🟢 Low Usage
- AI-generated recommendations:
  - Energy-saving tips
  - Cost optimization guidance
  - Explanations of why suggestions are effective
- Works as a **CLI tool** with interactive or argument-based input.

---

## 🛠 Installation

### 1. Clone Repository
```bash
git clone https://github.com/yourusername/smart-home-energy-ai.git
cd smart-home-energy-ai
2. Install Dependencies
bash
Copy code
pip install numpy pandas statsmodels google-generativeai argparse
3. Configure API Key
Open the script and replace with your Gemini API key:

python
Copy code
genai.configure(api_key="YOUR_GEMINI_API_KEY")
📌 Usage
CLI Mode
Provide usage values (space-separated):

bash
Copy code
python energy_ai.py --usage "8 7.5 9 10 11 12 13"
Interactive Mode
If no arguments are provided:

bash
Copy code
python energy_ai.py
Then enter:

pgsql
Copy code
Enter home energy usage in kWh separated by spaces (at least 5 values):
5 6 7 8 9 10
📊 Example Output
vbnet
Copy code
🏠 Smart Home Energy Forecast & AI Recommendations
------------------------------------------------------------
Next 5 Forecasted Consumption (kWh): [10.5, 11.2, 12.1, 12.8, 13.6]
Trend                               : increasing 📈
Usage Level                         : High Energy Usage 🔴

🤖 AI Recommendations:
Switch to LED lights and optimize AC usage with smart thermostats.

AI Explanation:
LEDs reduce electricity by 75% compared to incandescent bulbs, and smart thermostats
can cut heating/cooling bills by up to 15%, making them highly cost-effective.
🔮 Future Enhancements
Add real-time energy data integration (smart meters / IoT).

Support for solar energy optimization.

Export insights to CSV/Excel/PDF.

Web dashboard with visualization (Flask + Chart.js).