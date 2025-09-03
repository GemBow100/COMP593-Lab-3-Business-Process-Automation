""" 
Description: 
  Divides sales data CSV file into individual order data Excel files.

Usage:
  python process_sales_data.py sales_csv_path

Parameters:
  sales_csv_path = Full path of the sales data CSV file
"""
from sys import argv
import os 
from datetime import date
import pandas as pd
import re
import csv

def main():
    sales_csv_path = get_sales_csv_path()
    orders_dir_path = create_orders_dir(sales_csv_path)
    process_sales_data(sales_csv_path, orders_dir_path)

def get_sales_csv_path():

    #Check whether command line parameter provided if it is not provided return an error message.
    num_params =len(argv)-1
    if num_params < 1:
        print("Error: Missing path to sales data CSV file")
        exit(1)
    #Check whether provide parameter is valid path of file if not provided an error message.
    sales_csv =argv[1]
    if not os.path.isfile(sales_csv):
        print("Error: invalid path to sales data CSV file.")
    # Return path of sales data CSV file
        return sales_csv
    
     

def create_orders_dir(sales_csv_path):
   
    # Get directory in which sales data CSV file resides
    sales_dir = os.path.dirname(os.path.abspath(sales_csv_path))
    # Determine the path of the directory to hold the order data files
    today_date= date.today().isoformat()
    orders_dir = os.path.join(sales_dir,f'Order {today_date}')
    # Create the orders directory if it does not already exist
    if not os.path.isdir(orders_dir):
        os.makedirs(orders_dir)
    # Return path of orders directory
        return orders_dir


def process_sales_data(sales_csv_path, orders_dir_path):
   
    # Import the sales data from the CSV file into a DataFrame
    with open("sales_data.csv") as file:
        reader = csv.reader(file)
        data = list(reader)
    # TODO: Insert a new "TOTAL PRICE" column into the DataFrame
    data [0].append('Total_Price')
    for row in data[1:]:
        row.append('Total_Price')

    # Remove columns from the DataFrame that are not needed
    sales_csv_path.drop(colums=['Status','Address', 'City','State','Postal Code', 'Country'])

    # Groups orders by ID and iterate and remove
    for order_id in sales_csv_path.groupby('Order ID'):
        order_id.drop('Order ID')
        # Sort the items by item number
        # Append a "GRAND TOTAL" row
        grand_total =order_id['Total Price'].sums()
        grand_total_df = pd.DataFrame({'ITEM PRICE':['GRAND TOTAL']|'TOTAL PRICE:' ['grand_total']})
        order_df = pd.concat ([order_id,grand_total_df])
        # Determine the file name and full path of the Excel sheet
        customer_name = order_df['customer_name'].values[0]
        customer_name = re.sub(r'\w', '', customer_name)
        order_file = f'Order{order_id}.{customer_name}.xlsx'
        order_path = os.path.join(orders_dir_path. order_file)

        # Export the data to an Excel sheet
        data = { order_file, order_path, grand_total,order_df, customer_name}
        df = pd.DataFrame(data)
        output_path = 'sales_data.xlsx'
        df.to_excel(output_path)
        # Format the Excel sheet
        workbook=workbook()
        sheet= workbook.active
        sheet["2"] = "Total Price"
        workbook.save(filename="Total Price")
        #Define format for the money columns
        money_fmt = "sale_data.xlsx"
        df = pd.read_excel(money_fmt)
        money_fmt = workbook.add_format({'num_format':'$a,00.00'})
        # Format each columns
        pd.set_option('max_columnwidth', 100)
        df =pd.DataFrame('sales_data.xlsx')
        print(df)
        #Close the Excelwriter 
        workbook.close()

    

if __name__ == '__main__':
    main()