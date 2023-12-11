import pandas as pd


def create_dataframe(data, field_names):
    """

    :param data:
    :param field_names:
    :return:
    """
    # Check if the length of field_names is three
    if len(field_names) != 3:
        raise ValueError("field_names should contain exactly three names.")

    df = pd.DataFrame(data, columns=field_names)
    return df


# Example usage:
data = [(1, 'A', 10),
        (2, 'B', 20),
        (3, 'C', 30)]

fields = ['Field1', 'Field2', 'Field3']

result_df = create_dataframe(data, fields)
print(result_df)
