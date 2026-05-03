import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1. Import data
df = pd.read_csv('medical_examination.csv')

# 2. Add overweight column
df['overweight'] = (df['weight'] / (df['height'] / 100) ** 2).apply(lambda x: 1 if x > 25 else 0)

# 3. Normalize cholesterol and gluc (0 = good, 1 = bad)
df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)


def draw_cat_plot():
    # 4. Create DataFrame for cat plot using pd.melt
    df_cat = pd.melt(
        df,
        id_vars=['cardio'],
        value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']
    )

    # 5. Group and reformat data, rename 'value' to 'total' for catplot
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')

    # 6. Draw cat plot
    fig = sns.catplot(
        data=df_cat,
        x='variable',
        y='total',
        hue='value',
        col='cardio',
        kind='bar'
    ).fig

    # 7. Do not modify
    fig.savefig('catplot.png')
    return fig


def draw_heat_map():
    # 8. Clean data
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # 9. Calculate correlation matrix
    corr = df_heat.corr()

    # 10. Generate mask for upper triangle
    mask = np.zeros_like(corr, dtype=bool)
    mask[np.triu_indices_from(mask)] = True

    # 11. Set up matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 10))

    # 12. Plot heatmap
    sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        fmt='.1f',
        center=0,
        square=True,
        linewidths=0.5,
        ax=ax,
        cbar_kws={'shrink': 0.5}
    )

    # 13. Do not modify
    fig.savefig('heatmap.png')
    return fig
