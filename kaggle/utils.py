def get_columns_with_missing_data(dataset):
    columns_with_null = []
    for column in dataset:
        if sum(dataset[column].isnull()) > 0:
            columns_with_null.append(column)
    return columns_with_null
