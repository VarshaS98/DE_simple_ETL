# DE_simple_ETL
Extract Transform Load Example using Python

Extract:
The extract function utilizes the requests library to fetch data from the API endpoint http://universities.hipolabs.com/search?country=United+States.
The obtained data, in JSON format, is returned for further processing.
Transform:
The transform function converts the extracted JSON data into a Pandas DataFrame.
It filters the DataFrame to include only universities in California and modifies the 'domains' and 'web_pages' columns.
The final DataFrame consists of selected columns: 'domains', 'country', 'web_pages', and 'name'.
Load:
The load function takes the transformed DataFrame and loads it into an SQLite database named "my_lite_store.db" using SQLAlchemy.
If the 'cal_uni' table already exists in the database, it is replaced.
Main Execution:
The script orchestrates the entire ETL process by calling the extract, transform, and load functions.
The result is a simple yet functional example of extracting, transforming, and loading data from an API into an SQLite database.
