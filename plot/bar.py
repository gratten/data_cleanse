def bar(df_key, indicator, path, totalFiles):
    title = f'Graph {indicator}\n {path}\n Total files: {totalFiles}'
    ax = df_key.plot.barh(y='occurences', x='paths', figsize=(5, 10), title=title)