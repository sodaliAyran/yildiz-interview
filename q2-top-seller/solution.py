import argparse
import pandas as pd
import heapq


def return_result_to_string(df, row_name, top):
    df = df.groupby([row_name])[['quantity']].agg('sum').reset_index()
    return df[df.quantity.isin(heapq.nlargest(top, df.quantity))].sort_values(by=['quantity'],
                                                                              ascending=False)[[row_name, 'quantity']].to_string(index=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--min-date',nargs='?', default="2020-01-01", type=str)
    parser.add_argument('--max-date',nargs='?', default="2020-06-30", type=str)
    parser.add_argument('--top', nargs='?', default=3, type=int)

    args = parser.parse_args()
    min_date = args.min_date
    max_date = args.max_date
    top = args.top

    product = pd.read_csv("product.csv", dtype={'id': 'int', 'name': 'str', 'brand': 'str'})
    sales = pd.read_csv("sales.csv", dtype={'product': 'int', 'store': 'int', 'quantity': 'int'}, parse_dates=['date'])
    store = pd.read_csv("store.csv", dtype={'id': 'int', 'name': 'str', 'city': 'str'})

    mask = (sales['date'] >= min_date) & (sales['date'] <= max_date)
    sales = sales.loc[mask]

    product_sales = pd.merge(product, sales, left_on=['id'], right_on=['product'])
    store_sales = pd.merge(store, sales, left_on=['id'], right_on=['store'])

    print("-- top seller product --")
    print(return_result_to_string(df=product_sales, row_name='name', top=top))

    print("-- top seller store --")
    print(return_result_to_string(df=store_sales, row_name='name', top=top))

    print("-- top seller brand --")
    print(return_result_to_string(df=product_sales, row_name='brand', top=top))

    print("-- top seller city --")
    print(return_result_to_string(df=store_sales, row_name='city', top=top))
