def index_finder(df,val):
    indices = np.where(df.values == val)
    idx=[]
    index_numbers = indices[0].tolist()
    column_numbers = indices[1].tolist()
    for k in range(len(index_numbers )):
        for t in range(len(column_numbers)):
            idx.append([int(index_numbers[k]),int(column_numbers[t])])
    return idx