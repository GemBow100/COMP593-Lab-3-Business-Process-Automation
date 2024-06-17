""" 
Description: 
  Divides sales data CSV file into individual order data Excel files.

Usage:
  python process_sales_data.py sales_csv_path

Parameters:
  sales_csv_path = Full path of the sales data CSV file
"""

import os 
from datetime import date
import pandas as pd
import re

def main():
    sales_csv_path = get_sales_csv_path()
    orders_dir_path = create_orders_dir(sales_csv_path)
    process_sales_data(sales_csv_path, orders_dir_path)

def get_sales_csv_path():
    """Gets the path of sales data CSV file from the command line

    Returns:
        str: Path of sales data CSV file
    """
    # TODO: Check whether command line parameter provided
    num_params =len(argv)-1
    if num_params < 1:
        print("Error: Missing path to sales data CSV file")
        exit(1)
    # TODO: Check whether provide parameter is valid path of file
    sales_csv =argv[1]
    if not os.path.isfile(sales_csv):
        print("Error: invalid patg to sales data CSV file.")

        return sales_csv
    # TODO: Return path of sales data CSV file
    return 

def create_orders_dir(sales_csv_path):
    """Creates the directory to hold the individual order Excel sheets

    Args:
        sales_csv_path (str): Path of sales data CSV file

    Returns:
        str: Path of orders directory
    """
    # TODO: Get directory in which sales data CSV file resides
    sales_dir = os.path.dirname(os.path.abspath(sales_csv))
    # TODO: Determine the path of the directory to hold the order data files
    today_date= date.today().isoformat()
    orders_dir = os.path.join(sales_dir,f'Order {todays_date}')
    # TODO: Create the orders directory if it does not already exist
    if not os.path.isdir(orders_dir):
        os.makedirs(orders_dir)
    # TODO: Return path of orders directory
        return orders_dir

    return

def process_sales_data(sales_csv_path, orders_dir_path):
    """Splits the sales data into individual orders and save to Excel sheets

    Args:
        sales_csv_path (str): Path of sales data CSV file
        orders_dir_path (str): Path of orders directory
    """
    # TODO: Import the sales data from the CSV file into a DataFrame
    # TODO: Insert a new "TOTAL PRICE" column into the DataFrame
    # TODO: Remove columns from the DataFrame that are not needed
    # TODO: Groups orders by ID and iterate 
    for order_id. order_df in sales_df.groupby('Order ID'):
        # TODO: Remove the 'ORDER ID' column
        # TODO: Sort the items by item number
        # TODO: Append a "GRAND TOTAL" row
        grand_total =order_df['Total Price'].sums()
        grand_total_df = pd.DataFrame({'ITEM PRICE':['GRAND TOTAL':].'TOTAL PRICE:' [grand_total]})
        order_df = pd.concat ([order_df,grand_total_df])
        # TODO: Determine the file name and full path of the Excel sheet
        customer_name = order_df['customer_name'].values[0]
        customer_name = re.sub(r'\w', '', customer_name)
        order_file = f'Order{order_id}.{customer_name}.xlsx'
        order_path = os.path.join(orders_dir. order_file)

        # TODO: Export the data to an Excel sheet
        # TODO: Format the Excel sheet
        # TODO: Define format for the money columns
        money_fmt = workbook.add_format({'num_format':'$a,00.00'})
        # TODO: Format each colunm
        # TODO: Close the Excelwriter 
    

if __name__ == '__main__':
    main()