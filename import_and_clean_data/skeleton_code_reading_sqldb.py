# Import packages
from sqlalchemy import create_engine
import pandas as pd

# ------------Method 1---------------

# Create engine: engine
engine = create_engine('sqlite:///mydb.sqlite')

# Open engine connection: con
con = engine.connect()

# Perform query: rs
rs = con.execute("SELECT * from Album")

# Save results of the query to DataFrame: df
df = pd.DataFrame(rs.fetchall())

# Close connection
con.close()

# Print head of DataFrame df
print(df.head())


# ------------Method 1 End ---------------

# ------------Method 2  -----------------

# Open engine in context manager
# Create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')

# Perform query and save results to DataFrame: df
with engine.connect() as con:
    rs = con.execute("Select LastName, Title from Employee")

    # select all the records, extracting the Title of the record and Name of the artist of
    # each record from the Album table and the Artist table, respectively.
    rs = con.execute("SELECT Title, Name FROM Album INNER JOIN Artist on Album.ArtistID = Artist.ArtistID")
    df = pd.DataFrame(rs.fetchmany(size=3))
    df.columns = rs.keys()

# Print the length of the DataFrame df
print(len(df))

# Print the head of the DataFrame df
print(df.head())

# ------------Method 3  -----------------
# Create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')

# Execute query and store records in DataFrame: df
df1 = pd.read_sql_query("SELECT * FROM Employee WHERE EmployeeId >= 6 ORDER BY BirthDate", engine)

# Print head of DataFrame
print(df1.head())