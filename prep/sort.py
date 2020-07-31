def chunk(df1, target):
    import pandas as pd
    df2 = pd.DataFrame(columns=df1.columns)

    col_count = len(df1.columns)

    for i in range(col_count):
        cond = df1.iloc[:, i] == target
        rows = df1.loc[cond, :]
        df2 = df2.append(rows, ignore_index=True)
        df1.drop(rows.index, inplace=True)

    inc = col_count - 1

    while inc >= 2:
        for i in range(len(df2)):
            if target == df2.iloc[i, inc]:
                varA = df2.iloc[i, 1]
                varB = df2.iloc[i, inc]
                df2.iloc[i, 1] = varB
                df2.iloc[i, inc] = varA
        inc -= 1

    df_collection = {}
    df_collection[0] = df1
    df_collection[1] = df2

    return df_collection


def chunk2(df):
    # recieves df columns = x (right now x = 3)
    # returns sorted df columns = x-1 and dropped column series

    # create the list
    col_count = len(df.columns)-1
    list = df.iloc[:, col_count]

    while col_count >= 2:
        col_count -= 1
        list = list.append(df.iloc[:, col_count])

    most_occuring = list.value_counts()
    chunk_collection = {}
    dropped_col_collection = {}

    for i in range(len(most_occuring)):
        target = most_occuring.index[i]
        chunk_out = chunk(df, target)
        df_chunk = chunk_out[1]
        df = chunk_out[0]  # leftover
        dropped_col = df_chunk.iloc[:, 1]
        dropped_col_collection[i] = dropped_col
        df_chunk = df_chunk.drop(df_chunk.columns[1], 1)
        chunk_collection[i] = df_chunk

    # clean up, remove values of length = 0
    chunk_collection = {k: v for k, v in chunk_collection.items() if len(v) > 0}


    # convert collection to list, as only a single value is needed to reset the dropped column
    # can be cleaned up and included in previous loop eventually
    dropped_col_list = []
    for key in dropped_col_collection.keys():
        if len(dropped_col_collection[key]) > 0:
            dropped_col_list.append(dropped_col_collection[key][0])

    return chunk_collection, dropped_col_list


def rebuild(df_collection, dropped_col_list, col_name):
    # recieves collection of sorted dataframes, dropped column
    # puts them together and adds back the dropped column
    # returns dataframe
    import pandas as pd

    inc = 0

    df_rebuild = pd.DataFrame(columns=df_collection[0].columns)
    for key in df_collection.keys():
        drop_col_val = dropped_col_list[inc]
        df_to_append = df_collection[key]
        df_to_append.insert(1, col_name, drop_col_val)
        df_rebuild = df_rebuild.append(df_to_append)
        inc += 1

    return df_rebuild


def generate_paths(dups, occur):
    # recieve list of duplicate files
    # restructure into following format, # of path columns dictated by occur value input
    # filename - path1 - path2 - path3 - path4...
    from collections import defaultdict
    import pandas as pd

    names = []
    paths = []

    for i in range(0, len(dups)):
        names.append(dups['Name'].iloc[i])
        paths.append(dups['path'].iloc[i])

    s = zip(names, paths)
    d = defaultdict(list)
    for k, v in s:
        d[k].append(v)

    # restructure into new df (pairs) containing only pairs of duplicate paths
    df_names = []
    path_collection = []
    path_list = []

    for k, v in d.items():
        if len(v) == occur:
            df_names.append(k)
            for path in v:
                path_list.append(path)
            path_collection.append(path_list)
            path_list = []

    col_list = []
    col = []
    for i in range(occur):
        for j in range(len(path_collection)):
            col.append(path_collection[j][i])
        col_list.append(col)
        col = []

    path_data = {'name': df_names}
    inc = 1
    for i in range(occur):
        col_name = 'path' + str(inc)
        path_data[col_name] = col_list[i]
        inc += 1

    paths = pd.DataFrame(data=path_data)
    paths = paths.sort_values(['name'])

    return paths