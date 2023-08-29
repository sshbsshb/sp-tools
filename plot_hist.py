import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# High-Resolution Output for Academic Papers
plt.rcParams["figure.dpi"] = 300

# Data Preparation
data = {
    'Parameters': ['nFin', 'Hslope', 'Wt1', 'Hcut', 'Wcut', 'Hcut2', 'Wcut2', 'Hcut3', 'Wcut3'],
    'DoE Sensitivities': [0.597864141, 0.597864141, 0.597864141, 0.599757152, 0.597864141, 0.526326465, 0.604912228, 0.636638546, 0.369439172],
    'Bayesian Importance': [0.29, 0, 0.26, 0.07, 0.31, 0.01, 0.02, 0.01, 0.03]
}
df = pd.DataFrame(data)

# Plot Configuration
fig, ax1 = plt.subplots(figsize=(12, 8))

# Enhanced Aesthetic Styles Using Seaborn
sns.set_style("white")
sns.set_context("paper", font_scale=1.2)

# Create the first histogram (DoE Sensitivities)
bar1 = ax1.bar(df['Parameters'], df['DoE Sensitivities'], color='steelblue', alpha=0.7, label='DoE Sensitivities', width=0.4)
ax1.set_xlabel('Parameters', fontsize=22)
ax1.tick_params(axis='x', labelsize=14)
ax1.set_ylabel('DoE Sensitivities', fontsize=24, color='steelblue')
ax1.tick_params(axis='y', labelcolor='steelblue', labelsize=14)

# Create the second axis object
ax2 = ax1.twinx()

# Create the second histogram (Bayesian Importance)
bar2 = ax2.bar(df['Parameters'], df['Bayesian Importance'], color='darkred', alpha=0.7, label='Bayesian Importance', width=0.4, align='edge')
ax2.set_ylabel('Bayesian Importance', fontsize=24, color='darkred')
ax2.tick_params(axis='y', labelcolor='darkred', labelsize=14)

# Add a legend
lines_labels = [bar1, bar2]
labels = [l.get_label() for l in lines_labels]
ax1.legend(lines_labels, labels, fontsize=22, loc='upper right')

# # Fine-tuning plot appearance
# sns.despine(right=False)
# plt.title('Comparison of DoE Sensitivities and Bayesian Importance', fontsize=16)

# Save as high-resolution image
plt.savefig('enhanced_two_axis_histogram.png')

# Show the plot
plt.show()
