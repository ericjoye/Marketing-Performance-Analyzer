# 📊 Marketing Performance Analyzer

A comprehensive Python-based analytics tool for evaluating marketing campaign performance, identifying optimization opportunities, and making data-driven budget allocation decisions.

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Production%20Ready-success.svg)

---

## 🎯 Business Use Case

Marketing teams spend significant budgets across multiple channels (social media, search engines, email, etc.) without always knowing which campaigns deliver the best return on investment. This analyzer helps:

- **Marketing Managers**: Identify which campaigns to scale up or shut down
- **Growth Teams**: Optimize budget allocation across channels
- **Executives**: Understand overall marketing efficiency and ROI
- **Data Analysts**: Generate actionable insights from campaign data

### Real-World Problems This Solves:

1. **Budget Waste**: Continuing to fund underperforming campaigns
2. **Missed Opportunities**: Not scaling campaigns with strong ROI
3. **Poor Visibility**: Lacking clear metrics to compare campaign performance
4. **Data Overload**: Having data but no actionable recommendations

---

## 📈 Key Metrics Explained

### 1. **CTR (Click-Through Rate)**
```
CTR = (Clicks / Impressions) × 100
```
- **What it measures**: How compelling your ad is to your target audience
- **Good benchmark**: 2-5% (varies by industry and channel)
- **Use case**: Evaluating ad creative effectiveness
- **Optimization**: Low CTR → Test new headlines, images, or targeting

### 2. **CPC (Cost Per Click)**
```
CPC = Total Spend / Total Clicks
```
- **What it measures**: Average cost to get someone to click your ad
- **Good benchmark**: $1-3 for most industries
- **Use case**: Evaluating traffic acquisition efficiency
- **Optimization**: High CPC → Improve Quality Score, refine targeting, test new keywords

### 3. **CPA (Cost Per Acquisition)**
```
CPA = Total Spend / Total Conversions
```
- **What it measures**: Average cost to acquire one customer/conversion
- **Good benchmark**: Should be lower than your Customer Lifetime Value (CLV)
- **Use case**: Determining campaign profitability
- **Optimization**: High CPA → Optimize landing pages, improve audience targeting

### 4. **Conversion Rate**
```
Conversion Rate = (Conversions / Clicks) × 100
```
- **What it measures**: Percentage of visitors who complete desired action
- **Good benchmark**: 2-10% (varies by industry)
- **Use case**: Evaluating landing page and offer effectiveness
- **Optimization**: Low conversion → A/B test landing pages, simplify checkout, improve messaging

### 5. **ROI (Return on Investment)**
```
ROI = ((Revenue - Spend) / Spend) × 100
```
- **What it measures**: Profitability of the campaign
- **Good benchmark**: Positive ROI (>0%) means profitable
- **Use case**: Overall campaign success measurement
- **Optimization**: Negative ROI → Pause campaign or implement all above optimizations

---

## 🚀 Getting Started

### Prerequisites

```bash
Python 3.7+
pip (Python package manager)
```

### Installation

1. **Clone the repository**:
```bash
git clone https://github.com/yourusername/marketing-performance-analyzer.git
cd marketing-performance-analyzer
```

2. **Install required packages**:
```bash
pip install pandas matplotlib
```

### Quick Start

1. **Run the analyzer**:
```bash
python analyzer.py
```

2. **View the results**:
   - Console output: Performance summary and recommendations
   - `campaign_performance_dashboard.png`: Visual dashboard
   - `campaign_analysis_results.csv`: Detailed metrics for all campaigns

---

## 📁 Project Structure

```
marketing-performance-analyzer/
│
├── sample_data.csv              # Sample campaign data (15 campaigns)
├── analyzer.py                  # Main analysis script
├── README.md                    # This file
│
├── Generated Outputs:
│   ├── campaign_analysis_results.csv      # Detailed results with rankings
│   └── campaign_performance_dashboard.png # Visual performance dashboard
```

---

## 💼 How Teams Use This Analysis

### For Marketing Managers:
1. **Daily/Weekly**: Monitor campaign performance trends
2. **Monthly**: Review ROI rankings and adjust budgets
3. **Quarterly**: Identify winning strategies to replicate

**Example Decision**: "Instagram Influencer campaign has 186% ROI. Let's increase its budget by 50% next month."

### For Growth Teams:
1. **Channel Optimization**: Compare performance across different platforms
2. **A/B Testing**: Track which variations perform better
3. **Budget Reallocation**: Move spend from low to high ROI campaigns

**Example Decision**: "Move 30% of budget from Brand Awareness (ROI: 100%) to TikTok Video Ads (ROI: 193%)."

### For Finance/Executives:
1. **Efficiency Reporting**: Overall marketing spend effectiveness
2. **Budget Planning**: Data-driven budget requests
3. **Performance Benchmarking**: Compare to industry standards

**Example Decision**: "Current average CPA is $11.23. Target is $9.50. Need to optimize bottom 5 campaigns."

### For Data Analysts:
1. **Deep Dive Analysis**: Investigate patterns in high/low performers
2. **Predictive Modeling**: Use historical data to forecast performance
3. **Attribution Analysis**: Understand which campaigns drive conversions

**Example Insight**: "Campaigns with CTR > 4% and conversion rate > 6% consistently achieve ROI > 150%."

---

## 🔍 Understanding the Output

### Console Output Sections:

#### 1. Performance Summary Table
- Shows all campaigns ranked by ROI
- Includes all key metrics for quick comparison
- Identify winners and losers at a glance

#### 2. Optimization Recommendations
- **Top Performers**: Campaigns to scale up
- **Underperformers**: Campaigns to optimize or pause
- **High Traffic, Low Conversion**: Landing page issues
- **Budget Allocation Insights**: Overall spend efficiency
- **Quick Wins**: Low-hanging fruit opportunities

#### 3. Visual Dashboard (4 Charts)
- **ROI Comparison**: Bar chart showing profitability
- **Cost Efficiency Matrix**: Scatter plot of CPA vs Conversion Rate
- **Spend vs Conversions**: Budget allocation effectiveness
- **CTR vs Conversion Rate**: Funnel performance comparison

---

## 🎨 Sample Insights from Analysis

### Example Findings:

```
✅ TOP PERFORMERS (Scale Up):
   1. Instagram_Influencer
      → ROI: 186.67% | CPA: $8.33 | Conversion Rate: 6.0%
      → Recommendation: Increase budget by 25-50% to maximize returns

⚠️  UNDERPERFORMERS (Optimize or Pause):
   15. YouTube_PreRoll
       → ROI: 3.92% | CPA: $18.75 | Conversion Rate: 4.0%
       → Low Conversion Rate: Optimize landing page or audience targeting

🎯 HIGH TRAFFIC, LOW CONVERSION (Landing Page Optimization Needed):
   • Social_Media_Boost
      → CTR: 4.0% (Good) | Conversion Rate: 5.0% (Needs Work)
      → Recommendation: A/B test landing pages, improve load speed, clarify CTA
```

---

## 🛠️ Customization

### Using Your Own Data:

1. **Prepare your CSV** with these columns:
   - `campaign_name`: Name of the campaign
   - `impressions`: Number of ad views
   - `clicks`: Number of clicks on ads
   - `conversions`: Number of successful conversions
   - `spend`: Total amount spent (in dollars)

2. **Update the analyzer** (optional):
   - Modify `avg_order_value` in `calculate_metrics()` function (line 65) to match your business
   - Adjust benchmark thresholds in recommendations
   - Customize visualization colors/style

3. **Run the analysis**:
```bash
python analyzer.py
```

---

## 📊 Advanced Usage

### Integrate with Your Data Pipeline:

```python
# Example: Load data from your database
import pandas as pd
from analyzer import calculate_metrics, rank_campaigns

# Connect to your database
df = pd.read_sql("SELECT * FROM campaigns WHERE date >= '2024-01-01'", conn)

# Run analysis
df_metrics = calculate_metrics(df)
df_ranked = rank_campaigns(df_metrics)

# Generate insights
df_ranked.to_csv('monthly_report.csv', index=False)
```

### Automate Monthly Reports:

```bash
# Add to cron job for monthly automation
0 9 1 * * cd /path/to/analyzer && python analyzer.py && mail -s "Monthly Campaign Report" team@company.com < campaign_analysis_results.csv
```

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Add new metrics**: ROAS, LTV/CAC ratio, attribution models
2. **Improve visualizations**: Interactive dashboards, more chart types
3. **Add data sources**: Connect to Google Analytics, Facebook Ads API
4. **Enhance recommendations**: ML-based predictive insights

### To Contribute:
```bash
1. Fork the repository
2. Create your feature branch: git checkout -b feature/AmazingFeature
3. Commit your changes: git commit -m 'Add some AmazingFeature'
4. Push to the branch: git push origin feature/AmazingFeature
5. Open a Pull Request
```

---

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 📞 Support

**Questions or Issues?**
- Open an issue on GitHub
- Contact: mail@ericjoye.com

---

## 🎓 Learning Resources

To get the most out of this tool, check out:

- [Google Analytics Academy](https://analytics.google.com/analytics/academy/)
- [Digital Marketing Metrics Guide](https://www.hubspot.com/marketing-statistics)
- [A/B Testing Best Practices](https://vwo.com/ab-testing/)
- [ROI Calculation Methods](https://blog.hubspot.com/marketing/marketing-roi)

---

## 🚀 Roadmap

### Upcoming Features:
- [ ] API integrations (Google Ads, Facebook Ads, LinkedIn Ads)
- [ ] Real-time dashboard with auto-refresh
- [ ] Predictive analytics for campaign forecasting
- [ ] Multi-touch attribution modeling
- [ ] Automated email reports
- [ ] Cohort analysis and customer segmentation
- [ ] Cost anomaly detection and alerts

---

## ⭐ Star This Repository

If you find this tool useful, please star the repository! It helps others discover it.

---

**Built with ❤️ by Eric Joye**

*Last Updated: January 2026*
