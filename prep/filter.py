def sld(df):
    # remove all non-sld rows, exclude drawings
    df1 = df[df['Format'] == 'SLDPRT']
    df2 = df[df['Format'] == 'SLDASM']
    df = df1.append([df2])
    df['name_low'] = df['Name'].str.lower()
    return df

def sld_drw(df):
    # remove all non-sld rows, include drawings
    df1 = df[df['Format'] == 'SLDPRT']
    df2 = df[df['Format'] == 'SLDASM']
    df3 = df[df['Format'] == 'SLDDRW']
    df = df1.append([df2, df3])
    df['name_low'] = df['Name'].str.lower()
    return df

def paths(target, df):
    # remove all non-sld rows, exclude drawings
    df1 = df[df['path1'] == target]
    df2 = df[df['path2'] == target]
    df3 = df[df['path3'] == target]
    df = df1.append([df2, df3])
    return df