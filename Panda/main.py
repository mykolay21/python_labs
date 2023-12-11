import pandas as pd
import cryptpandas as crp


if __name__ == '__main__':
    df = pd.DataFrame({'A': [1, 2, 3],
                       'B': ['one', 'one', 'four']})

    crp.to_encrypted(df, password='mypassword123', path='file.crypt')

    decrypted_df = crp.read_encrypted(path='file.crypt', password='mypassword123')
