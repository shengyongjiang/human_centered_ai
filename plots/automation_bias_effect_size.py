#!/usr/bin/env python3
"""
Plot 3: Automation Bias Effect Size (Horizontal Bar Chart)
Shows performance difference from baseline (no alerts) for each testcase
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

# Calculate effect sizes (difference from baseline)
testcases = list(data.keys())
low_freq_effects = []
high_freq_effects = []

for testcase in testcases:
    baseline = data[testcase]['no_alert']
    low_freq_effect = data[testcase]['low_freq'] - baseline
    high_freq_effect = data[testcase]['high_freq'] - baseline
    
    low_freq_effects.append(low_freq_effect)
    high_freq_effects.append(high_freq_effect)

# Set up the plot
fig, ax = plt.subplots(figsize=(12, 8))

y_pos = np.arange(len(testcases))
bar_height = 0.35

# Create horizontal bars
bars_low = ax.barh(y_pos - bar_height/2, low_freq_effects, bar_height, 
                   label='Low Frequency vs No Alerts', color='#2E86AB', alpha=0.8,
                   edgecolor='black', linewidth=1)

bars_high = ax.barh(y_pos + bar_height/2, high_freq_effects, bar_height,
                    label='High Frequency vs No Alerts', color='#F18F01', alpha=0.8,
                    edgecolor='black', linewidth=1)

# Customize the plot
ax.set_xlabel('Performance Change from Baseline (%)', fontsize=14, fontweight='bold')
ax.set_ylabel('TestCase', fontsize=14, fontweight='bold')
ax.set_title('Automation Bias Effect Size by TestCase\n(Performance Change from No Alerts Baseline)', 
             fontsize=16, fontweight='bold', pad=20)
ax.set_yticks(y_pos)
ax.set_yticklabels(testcases)

# Add value labels on bars
for i, (bar_low, bar_high, low_effect, high_effect) in enumerate(zip(bars_low, bars_high, low_freq_effects, high_freq_effects)):
    # Low frequency bars
    width_low = bar_low.get_width()
    label_x_low = width_low + 0.5 if width_low >= 0 else width_low - 0.5
    ax.text(label_x_low, bar_low.get_y() + bar_low.get_height()/2,
            f'{low_effect:+.1f}%', ha='left' if width_low >= 0 else 'right', 
            va='center', fontweight='bold', fontsize=10)
    
    # High frequency bars
    width_high = bar_high.get_width()
    label_x_high = width_high + 0.5 if width_high >= 0 else width_high - 0.5
    ax.text(label_x_high, bar_high.get_y() + bar_high.get_height()/2,
            f'{high_effect:+.1f}%', ha='left' if width_high >= 0 else 'right', 
            va='center', fontweight='bold', fontsize=10)

# Add vertical line at x=0 (baseline)
ax.axvline(x=0, color='black', linestyle='-', linewidth=2, alpha=0.8)

# Add legend
ax.legend(loc='lower right', fontsize=12, frameon=True, fancybox=True, shadow=True)

# Add grid
ax.grid(True, alpha=0.3, axis='x')
ax.set_axisbelow(True)

# Color-code the background regions
ax.axvspan(-25, 0, alpha=0.1, color='red', label='Performance Decrease')
ax.axvspan(0, 15, alpha=0.1, color='green', label='Performance Increase')

# Add annotations
ax.annotate('Automation Bias\n(Performance Degradation)', 
            xy=(-15, 3.5), ha='center', va='center',
            fontsize=12, fontweight='bold',
            bbox=dict(boxstyle="round,pad=0.5", facecolor='lightcoral', alpha=0.7))

ax.annotate('Performance\nImprovement', 
            xy=(5, 2.2), ha='center', va='center',
            fontsize=12, fontweight='bold',
            bbox=dict(boxstyle="round,pad=0.5", facecolor='lightgreen', alpha=0.7))

# Set x-axis limits
ax.set_xlim(-25, 15)

plt.tight_layout()
plt.savefig('automation_bias_effect_size.png', dpi=300, bbox_inches='tight')
plt.show()

print("Plot 3 created: automation_bias_effect_size.png")
print("\nAutomation bias effect sizes:")
print("TestCase | Low Freq Effect | High Freq Effect")
print("-" * 45)
for i, testcase in enumerate(testcases):
    print(f"{testcase:<9} | {low_freq_effects[i]:>+6.1f}%        | {high_freq_effects[i]:>+7.1f}%")

print(f"\nAverage effect sizes:")
print(f"Low frequency alerts:  {np.mean(low_freq_effects):+.1f}%")
print(f"High frequency alerts: {np.mean(high_freq_effects):+.1f}%")