def data1(dups, num):
    top_offenders = dups['path'].value_counts().index.to_list()
    directory = top_offenders[num]

    file_list = []
    for i in range(len(dups['path'])):
        if dups['path'][i] == top_offenders[num]:
            file_list.append(dups['name_low'].iloc[i])

    file_paths = {}
    for file in file_list:
        dups_trimmed = dups[(dups['name_low'] == file)]
        path_list = []
        for path in dups_trimmed['path']:
            path_list.append(path)
        file_paths[file] = path_list

    totalFiles = 0
    for k, v in file_paths.items():
        totalFiles += len(v)

    occur_list = []
    for k, v in file_paths.items():
        if len(v) not in occur_list:
            occur_list.append(len(v))

    occur_dict = {}
    for i in occur_list:
        occur_dict[i] = 0
        for v in file_paths.values():
            if i == len(v):
                occur_dict[i] += 1

    num_list = []
    occur_list = []
    for i in range(len(occur_dict)):
        key = min(occur_dict.keys())
        num_list.append(key)
        value = occur_dict.pop(key)
        occur_list.append(value)

    return num_list, occur_list, totalFiles, file_paths