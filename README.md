# Data Warehouse (Udacity Project)

## Introduction
A music streaming startup, Sparkify, has grown their user base and song database and want to move their processes and data onto the cloud. Their data resides in S3, in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

## Project
### Requirements
- Access to AWS Redshift services
- Python 3
- Install pyscog2: `pip install psycopg2`
- Fill in the appropiate values in the `dwh.cfg` file

### Create Table Schemas
Execute the script: _create_tables.py_: 
```
python create_tables.py
```
This will connect to the Redshift cluster and execute the needed queries to
create the following tables in the database:
- staging_events
- staging_songs
- songplays
- users
- songs
- artists
- time



### Build ETL Pipeline
Execute the script: _etl.py_: 
```
python etl.py
```
This will connect to the Redshift cluster and load the data stored in S3:
- Song data: `s3://udacity-dend/song_data`
- Log data: `s3://udacity-dend/log_data`

into the staging tables: `staging_events` and `staging_songs` and from them it
will copy the data into the other tables
