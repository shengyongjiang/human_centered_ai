#!/usr/bin/env python3
"""
Plot 2: Alert Frequency Impact by Testcase (Line Plot)
Shows individual lines for each testcase demonstrating how performance changes with alert frequency
"""

import matplotlib.pyplot as plt
import numpy as np

# Data extracted from result.md
data = {
    'TestCase 1': {
        'no_alert': 100.0,
        'low_freq': 100.0, 
        'high_freq': 81.8
    },
    'TestCase 2': {
        'no_alert': 97.9,
        'low_freq': 93.6,
        'high_freq': 93.6
    },
    'TestCase 3': {
        'no_alert': 87.2,
        'low_freq': 95.7,
        'high_freq': 74.5
    },
    'TestCase 4': {
        'no_alert': 100.0,
        'low_freq': 89.4,
        'high_freq': 89.4
    }
}

# Set up the plot
fig, ax = plt.subplots(figsize=(12, 8))

conditions = ['No Alerts', 'Low Frequency', 'High Frequency']
x_pos = np.arange(len(conditions))

# Colors and markers for each testcase
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
markers = ['o', 's', '^', 'D']
linestyles = ['-', '--', '-.', ':']

# Plot each testcase
for i, (testcase, color, marker, linestyle) in enumerate(zip(data.keys(), colors, markers, linestyles)):
    y_values = [data[testcase]['no_alert'], data[testcase]['low_freq'], data[testcase]['high_freq']]
    
    ax.plot(x_pos, y_values, color=color, marker=marker, linestyle=linestyle,
            linewidth=3, markersize=10, label=testcase, markeredgecolor='black', markeredgewidth=1)
    
    # Add value labels
    for j, (x, y) in enumerate(zip(x_pos, y_values)):
        ax.annotate(f'{y:.1f}%', (x, y), textcoords="offset points", 
                   xytext=(0,10), ha='center', fontsize=10, fontweight='bold',
                   bbox=dict(boxstyle="round,pad=0.2", facecolor=color, alpha=0.3))

# Customize the plot
ax.set_xlabel('Alert Condition', fontsize=14, fontweight='bold')
ax.set_ylabel('Performance Accuracy (%)', fontsize=14, fontweight='bold')
ax.set_title('Performance Trends by TestCase\n(Individual Automation Bias Patterns)', 
             fontsize=16, fontweight='bold', pad=20)
ax.set_xticks(x_pos)
ax.set_xticklabels(conditions)
ax.set_ylim(70, 105)

# Add legend
ax.legend(loc='upper right', fontsize=12, frameon=True, fancybox=True, shadow=True)

# Add grid
ax.grid(True, alpha=0.3)
ax.set_axisbelow(True)

# Highlight automation bias patterns
ax.annotate('TestCase 1 & 3:\nStrong automation bias\nwith high frequency alerts', 
            xy=(2, 78), xytext=(1.2, 72),
            arrowprops=dict(arrowstyle='->', color='red', lw=2),
            fontsize=11, ha='center',
            bbox=dict(boxstyle="round,pad=0.3", facecolor='lightcoral', alpha=0.7))

ax.annotate('TestCase 3:\nLow freq alerts\nimprove performance', 
            xy=(1, 95.7), xytext=(0.3, 102),
            arrowprops=dict(arrowstyle='->', color='green', lw=2),
            fontsize=11, ha='center',
            bbox=dict(boxstyle="round,pad=0.3", facecolor='lightgreen', alpha=0.7))

plt.tight_layout()
plt.savefig('testcase_performance_trends.png', dpi=300, bbox_inches='tight')
plt.show()

print("Plot 2 created: testcase_performance_trends.png")
print("\nPerformance trends by testcase:")
for testcase in data:
    no_alert = data[testcase]['no_alert']
    high_freq = data[testcase]['high_freq']
    bias_effect = high_freq - no_alert
    print(f"{testcase}: {no_alert:.1f}% → {high_freq:.1f}% (Δ{bias_effect:+.1f}%)")