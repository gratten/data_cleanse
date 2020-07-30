def pie(df_input, fileName, totalFiles, titlestring):

    if titlestring == 1:
        titlestring = '\nTotal files:\n'
    elif titlestring == 2:
        titlestring = '\nUnique filenames:\n'
    elif titlestring == 3:
        titlestring = '\nUnique filenames existing more than 1x:\n'

    title = fileName + titlestring + totalFiles
    plot_dups_ = df_input.plot.pie(y='occurences', figsize=(10, 10), title=title)