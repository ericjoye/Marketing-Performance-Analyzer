"""
Marketing Performance Analyzer
===============================
A comprehensive tool for analyzing campaign performance and identifying optimization opportunities.

Author: Data Analytics Team
Version: 1.0.0
"""

import pandas as pd
import matplotlib.pyplot as plt
import sys

def load_campaign_data(filepath):
    """
    Load campaign data from CSV file.
    
    Args:
        filepath (str): Path to the CSV file containing campaign data
        
    Returns:
        pd.DataFrame: Loaded campaign data
    """
    try:
        df = pd.read_csv(filepath)
        print(f"✓ Successfully loaded {len(df)} campaigns\n")
        return df
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error loading data: {e}")
        sys.exit(1)

def calculate_metrics(df):
    """
    Calculate key marketing performance metrics for each campaign.
    
    Metrics calculated:
    - CTR (Click-Through Rate): (Clicks / Impressions) × 100
      Measures how effective the ad is at generating clicks
      
    - CPC (Cost Per Click): Spend / Clicks
      Average cost for each click received
      
    - CPA (Cost Per Acquisition): Spend / Conversions
      Average cost to acquire one customer/conversion
      
    - Conversion Rate: (Conversions / Clicks) × 100
      Percentage of clicks that result in conversions
      
    - ROI (Return on Investment): ((Revenue - Spend) / Spend) × 100
      Assuming $50 average order value for demonstration
      
    Args:
        df (pd.DataFrame): DataFrame with campaign data
        
    Returns:
        pd.DataFrame: DataFrame with calculated metrics
    """
    # Create a copy to avoid modifying original data
    df_metrics = df.copy()
    
    # CTR: Click-Through Rate (%)
    # Higher is better - indicates ad relevance and appeal
    df_metrics['CTR'] = (df_metrics['clicks'] / df_metrics['impressions']) * 100
    
    # CPC: Cost Per Click ($)
    # Lower is better - indicates efficient traffic acquisition
    df_metrics['CPC'] = df_metrics['spend'] / df_metrics['clicks']
    
    # CPA: Cost Per Acquisition ($)
    # Lower is better - indicates efficient customer acquisition
    df_metrics['CPA'] = df_metrics['spend'] / df_metrics['conversions']
    
    # Conversion Rate (%)
    # Higher is better - indicates landing page effectiveness and audience quality
    df_metrics['conversion_rate'] = (df_metrics['conversions'] / df_metrics['clicks']) * 100
    
    # ROI: Return on Investment (%)
    # Assuming $50 average order value (this should be customized for your business)
    avg_order_value = 50
    revenue = df_metrics['conversions'] * avg_order_value
    df_metrics['ROI'] = ((revenue - df_metrics['spend']) / df_metrics['spend']) * 100
    
    # Round all metrics for readability
    df_metrics['CTR'] = df_metrics['CTR'].round(2)
    df_metrics['CPC'] = df_metrics['CPC'].round(2)
    df_metrics['CPA'] = df_metrics['CPA'].round(2)
    df_metrics['conversion_rate'] = df_metrics['conversion_rate'].round(2)
    df_metrics['ROI'] = df_metrics['ROI'].round(2)
    
    return df_metrics

def rank_campaigns(df_metrics):
    """
    Rank campaigns from best to worst based on ROI.
    ROI is the most comprehensive metric as it accounts for both cost and return.
    
    Args:
        df_metrics (pd.DataFrame): DataFrame with calculated metrics
        
    Returns:
        pd.DataFrame: Sorted DataFrame with ranking
    """
    # Sort by ROI (descending - higher is better)
    df_ranked = df_metrics.sort_values('ROI', ascending=False).reset_index(drop=True)
    df_ranked.insert(0, 'rank', range(1, len(df_ranked) + 1))
    
    return df_ranked

def print_performance_summary(df_ranked):
    """
    Print a formatted summary of campaign performance.
    
    Args:
        df_ranked (pd.DataFrame): Ranked campaigns with metrics
    """
    print("=" * 100)
    print("MARKETING PERFORMANCE SUMMARY")
    print("=" * 100)
    print()
    
    # Display key columns in a readable format
    display_cols = ['rank', 'campaign_name', 'impressions', 'clicks', 'conversions', 
                    'spend', 'CTR', 'CPC', 'CPA', 'conversion_rate', 'ROI']
    
    # Format the output
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 30)
    
    print(df_ranked[display_cols].to_string(index=False))
    print()
    print("=" * 100)
    print()

def generate_recommendations(df_ranked):
    """
    Generate actionable optimization recommendations based on campaign performance.
    
    Args:
        df_ranked (pd.DataFrame): Ranked campaigns with metrics
    """
    print("📊 OPTIMIZATION RECOMMENDATIONS")
    print("=" * 100)
    print()
    
    # 1. Top Performers - Scale these campaigns
    top_3 = df_ranked.head(3)
    print("✅ TOP PERFORMERS (Scale Up):")
    print("-" * 100)
    for idx, row in top_3.iterrows():
        print(f"   {row['rank']}. {row['campaign_name']}")
        print(f"      → ROI: {row['ROI']}% | CPA: ${row['CPA']} | Conversion Rate: {row['conversion_rate']}%")
        print(f"      → Recommendation: Increase budget by 25-50% to maximize returns")
    print()
    
    # 2. Bottom Performers - Needs improvement
    bottom_3 = df_ranked.tail(3)
    print("⚠️  UNDERPERFORMERS (Optimize or Pause):")
    print("-" * 100)
    for idx, row in bottom_3.iterrows():
        print(f"   {row['rank']}. {row['campaign_name']}")
        print(f"      → ROI: {row['ROI']}% | CPA: ${row['CPA']} | Conversion Rate: {row['conversion_rate']}%")
        
        # Specific recommendations based on metrics
        if row['CTR'] < df_ranked['CTR'].median():
            print(f"      → Low CTR ({row['CTR']}%): Test new ad creative, headlines, or targeting")
        if row['conversion_rate'] < df_ranked['conversion_rate'].median():
            print(f"      → Low Conversion Rate ({row['conversion_rate']}%): Optimize landing page or audience targeting")
        if row['ROI'] < 0:
            print(f"      → Negative ROI: Consider pausing and reallocating budget")
    print()
    
    # 3. High CTR but Low Conversion Rate - Landing page issues
    high_ctr_low_conv = df_ranked[
        (df_ranked['CTR'] > df_ranked['CTR'].quantile(0.75)) &
        (df_ranked['conversion_rate'] < df_ranked['conversion_rate'].median())
    ]
    
    if not high_ctr_low_conv.empty:
        print("🎯 HIGH TRAFFIC, LOW CONVERSION (Landing Page Optimization Needed):")
        print("-" * 100)
        for idx, row in high_ctr_low_conv.iterrows():
            print(f"   • {row['campaign_name']}")
            print(f"      → CTR: {row['CTR']}% (Good) | Conversion Rate: {row['conversion_rate']}% (Needs Work)")
            print(f"      → Recommendation: A/B test landing pages, improve load speed, clarify CTA")
        print()
    
    # 4. Budget Allocation Insights
    total_spend = df_ranked['spend'].sum()
    total_conversions = df_ranked['conversions'].sum()
    avg_cpa = total_spend / total_conversions
    
    print("💰 BUDGET ALLOCATION INSIGHTS:")
    print("-" * 100)
    print(f"   • Total Spend: ${total_spend:,.2f}")
    print(f"   • Total Conversions: {total_conversions:,}")
    print(f"   • Average CPA: ${avg_cpa:.2f}")
    print()
    
    # Calculate potential savings
    efficient_campaigns = df_ranked[df_ranked['CPA'] < avg_cpa]
    inefficient_campaigns = df_ranked[df_ranked['CPA'] > avg_cpa]
    
    print(f"   • {len(efficient_campaigns)} campaigns performing ABOVE average (CPA < ${avg_cpa:.2f})")
    print(f"   • {len(inefficient_campaigns)} campaigns performing BELOW average (CPA > ${avg_cpa:.2f})")
    print()
    print(f"   → Recommendation: Shift budget from below-average to above-average campaigns")
    print(f"      to potentially reduce overall CPA by 15-30%")
    print()
    
    # 5. Quick Wins
    print("⚡ QUICK WINS:")
    print("-" * 100)
    
    # Campaigns with good ROI but low spend
    quick_wins = df_ranked[
        (df_ranked['ROI'] > df_ranked['ROI'].median()) &
        (df_ranked['spend'] < df_ranked['spend'].median())
    ]
    
    if not quick_wins.empty:
        print("   • Scale up these profitable low-spend campaigns:")
        for idx, row in quick_wins.iterrows():
            print(f"      - {row['campaign_name']}: ROI {row['ROI']}% at only ${row['spend']} spend")
    else:
        print("   • No obvious quick wins identified. Focus on optimizing underperformers.")
    
    print()
    print("=" * 100)
    print()

def create_visualization(df_ranked):
    """
    Create a comprehensive visualization comparing campaign performance.
    
    Args:
        df_ranked (pd.DataFrame): Ranked campaigns with metrics
    """
    # Create figure with subplots
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    fig.suptitle('Marketing Performance Dashboard', fontsize=18, fontweight='bold', y=0.995)
    
    # Color scheme
    colors = plt.cm.RdYlGn(df_ranked['ROI'] / df_ranked['ROI'].max())
    
    # 1. ROI Comparison (Top Left)
    ax1 = axes[0, 0]
    bars1 = ax1.barh(df_ranked['campaign_name'], df_ranked['ROI'], color=colors)
    ax1.set_xlabel('ROI (%)', fontweight='bold', fontsize=11)
    ax1.set_title('Return on Investment by Campaign', fontweight='bold', fontsize=12, pad=10)
    ax1.axvline(x=0, color='black', linestyle='-', linewidth=0.8)
    ax1.grid(axis='x', alpha=0.3, linestyle='--')
    ax1.set_xlim(df_ranked['ROI'].min() - 50, df_ranked['ROI'].max() + 50)
    
    # Add value labels
    for i, (bar, value) in enumerate(zip(bars1, df_ranked['ROI'])):
        ax1.text(value + 10, bar.get_y() + bar.get_height()/2, 
                f'{value:.1f}%', va='center', fontsize=9, fontweight='bold')
    
    # 2. Cost Efficiency: CPA vs Conversion Rate (Top Right)
    ax2 = axes[0, 1]
    scatter = ax2.scatter(df_ranked['conversion_rate'], df_ranked['CPA'], 
                         s=df_ranked['conversions']*2, c=df_ranked['ROI'], 
                         cmap='RdYlGn', alpha=0.6, edgecolors='black', linewidth=1.5)
    ax2.set_xlabel('Conversion Rate (%)', fontweight='bold', fontsize=11)
    ax2.set_ylabel('Cost Per Acquisition ($)', fontweight='bold', fontsize=11)
    ax2.set_title('Cost Efficiency Matrix', fontweight='bold', fontsize=12, pad=10)
    ax2.grid(True, alpha=0.3, linestyle='--')
    
    # Add median lines to show quadrants
    median_conv = df_ranked['conversion_rate'].median()
    median_cpa = df_ranked['CPA'].median()
    ax2.axvline(x=median_conv, color='gray', linestyle='--', linewidth=1, alpha=0.5)
    ax2.axhline(y=median_cpa, color='gray', linestyle='--', linewidth=1, alpha=0.5)
    
    # Add quadrant labels
    ax2.text(df_ranked['conversion_rate'].max() * 0.8, df_ranked['CPA'].min() * 1.2, 
            'IDEAL', fontsize=10, fontweight='bold', color='green', alpha=0.5)
    ax2.text(df_ranked['conversion_rate'].max() * 0.8, df_ranked['CPA'].max() * 0.9, 
            'HIGH COST', fontsize=10, fontweight='bold', color='orange', alpha=0.5)
    
    plt.colorbar(scatter, ax=ax2, label='ROI (%)')
    
    # 3. Spend vs Conversions (Bottom Left)
    ax3 = axes[1, 0]
    bars3 = ax3.bar(range(len(df_ranked)), df_ranked['spend'], 
                    color='steelblue', alpha=0.7, label='Spend ($)', edgecolor='black', linewidth=1)
    ax3_twin = ax3.twinx()
    line3 = ax3_twin.plot(range(len(df_ranked)), df_ranked['conversions'], 
                          color='darkgreen', marker='o', linewidth=2.5, 
                          markersize=8, label='Conversions', markeredgecolor='black', markeredgewidth=1)
    
    ax3.set_xlabel('Campaign', fontweight='bold', fontsize=11)
    ax3.set_ylabel('Spend ($)', color='steelblue', fontweight='bold', fontsize=11)
    ax3_twin.set_ylabel('Conversions', color='darkgreen', fontweight='bold', fontsize=11)
    ax3.set_title('Spend vs Conversions', fontweight='bold', fontsize=12, pad=10)
    ax3.set_xticks(range(len(df_ranked)))
    ax3.set_xticklabels(range(1, len(df_ranked)+1))
    ax3.grid(axis='y', alpha=0.3, linestyle='--')
    ax3.tick_params(axis='y', labelcolor='steelblue')
    ax3_twin.tick_params(axis='y', labelcolor='darkgreen')
    
    # 4. CTR vs Conversion Rate (Bottom Right)
    ax4 = axes[1, 1]
    x = range(len(df_ranked))
    width = 0.35
    bars4_1 = ax4.bar([i - width/2 for i in x], df_ranked['CTR'], 
                      width, label='CTR (%)', color='coral', alpha=0.8, edgecolor='black', linewidth=1)
    bars4_2 = ax4.bar([i + width/2 for i in x], df_ranked['conversion_rate'], 
                      width, label='Conversion Rate (%)', color='lightseagreen', alpha=0.8, 
                      edgecolor='black', linewidth=1)
    
    ax4.set_xlabel('Campaign (Ranked by ROI)', fontweight='bold', fontsize=11)
    ax4.set_ylabel('Percentage (%)', fontweight='bold', fontsize=11)
    ax4.set_title('Click-Through vs Conversion Rates', fontweight='bold', fontsize=12, pad=10)
    ax4.set_xticks(x)
    ax4.set_xticklabels(range(1, len(df_ranked)+1))
    ax4.legend(loc='upper right', fontsize=10)
    ax4.grid(axis='y', alpha=0.3, linestyle='--')
    
    plt.tight_layout()
    
    # Save the visualization
    output_file = '/home/claude/campaign_performance_dashboard.png'
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"✓ Visualization saved: {output_file}")
    print()
    
    return output_file

def main():
    """
    Main execution function.
    """
    print()
    print("=" * 100)
    print(" " * 35 + "MARKETING PERFORMANCE ANALYZER")
    print("=" * 100)
    print()
    
    # 1. Load data
    print("📁 Loading campaign data...")
    df = load_campaign_data('sample_data.csv')
    
    # 2. Calculate metrics
    print("🔢 Calculating performance metrics...")
    df_metrics = calculate_metrics(df)
    print("✓ Metrics calculated: CTR, CPC, CPA, Conversion Rate, ROI\n")
    
    # 3. Rank campaigns
    print("📊 Ranking campaigns by ROI...")
    df_ranked = rank_campaigns(df_metrics)
    print("✓ Campaigns ranked from best to worst\n")
    
    # 4. Display results
    print_performance_summary(df_ranked)
    
    # 5. Generate recommendations
    generate_recommendations(df_ranked)
    
    # 6. Create visualization
    print("📈 Creating performance dashboard...")
    viz_file = create_visualization(df_ranked)
    
    # 7. Save detailed report
    output_csv = '/home/claude/campaign_analysis_results.csv'
    df_ranked.to_csv(output_csv, index=False)
    print(f"✓ Detailed results saved: {output_csv}")
    print()
    
    print("=" * 100)
    print("Analysis complete! Review the recommendations above and the visualization.")
    print("=" * 100)
    print()

if __name__ == "__main__":
    main()
