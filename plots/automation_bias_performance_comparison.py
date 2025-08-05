#!/usr/bin/env python3
"""
Plot 1: Performance by Alert Condition (Bar Chart)
Shows average performance across all testcases for different alert conditions
"""

import matplotlib.pyplot as plt
import numpy as np

# Data extracted from result.md
data = {
    'testcase1': {
        'no_alert': 100.0,
        'low_freq': 100.0, 
        'high_freq': 81.8
    },
    'testcase2': {
        'no_alert': 97.9,
        'low_freq': 93.6,
        'high_freq': 93.6
    },
    'testcase3': {
        'no_alert': 87.2,
        'low_freq': 95.7,
        'high_freq': 74.5
    },
    'testcase4': {
        'no_alert': 100.0,
        'low_freq': 89.4,
        'high_freq': 89.4
    }
}

# Calculate averages and individual data points
conditions = ['No Alerts', 'Low Frequency', 'High Frequency']
averages = []
all_data = {'No Alerts': [], 'Low Frequency': [], 'High Frequency': []}

for testcase in data:
    all_data['No Alerts'].append(data[testcase]['no_alert'])
    all_data['Low Frequency'].append(data[testcase]['low_freq'])
    all_data['High Frequency'].append(data[testcase]['high_freq'])

averages = [np.mean(all_data[condition]) for condition in conditions]
std_devs = [np.std(all_data[condition]) for condition in conditions]

# Create the plot
fig, ax = plt.subplots(figsize=(10, 7))

# Bar chart
x_pos = np.arange(len(conditions))
bars = ax.bar(x_pos, averages, yerr=std_devs, capsize=5, 
              color=['#2E86AB', '#A23B72', '#F18F01'], 
              alpha=0.8, edgecolor='black', linewidth=1)

# Add individual data points
for i, condition in enumerate(conditions):
    y_values = all_data[condition]
    x_values = [i] * len(y_values)
    ax.scatter(x_values, y_values, color='red', s=50, zorder=5, alpha=0.7)

# Customize the plot
ax.set_xlabel('Alert Condition', fontsize=14, fontweight='bold')
ax.set_ylabel('Performance Accuracy (%)', fontsize=14, fontweight='bold')
ax.set_title('Performance by Alert Condition\n(Automation Bias Effect)', fontsize=16, fontweight='bold', pad=20)
ax.set_xticks(x_pos)
ax.set_xticklabels(conditions)
ax.set_ylim(70, 105)

# Add value labels on bars
for i, (bar, avg, std) in enumerate(zip(bars, averages, std_devs)):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height + std + 1,
            f'{avg:.1f}%', ha='center', va='bottom', fontweight='bold', fontsize=12)

# Add grid
ax.grid(True, alpha=0.3, axis='y')
ax.set_axisbelow(True)

# Add automation bias annotation
ax.annotate('Automation Bias:\nHigh frequency alerts\nreduce performance', 
            xy=(2, 87), xytext=(1.5, 75),
            arrowprops=dict(arrowstyle='->', color='red', lw=2),
            fontsize=11, ha='center', 
            bbox=dict(boxstyle="round,pad=0.3", facecolor='lightcoral', alpha=0.7))

plt.tight_layout()
plt.savefig('automation_bias_performance_comparison.png', dpi=300, bbox_inches='tight')
plt.show()

print("Plot 1 created: automation_bias_performance_comparison.png")
print(f"Average performance - No Alerts: {averages[0]:.1f}%")
print(f"Average performance - Low Frequency: {averages[1]:.1f}%") 
print(f"Average performance - High Frequency: {averages[2]:.1f}%")
print(f"Automation bias effect (High vs No): {averages[2] - averages[0]:.1f}%")