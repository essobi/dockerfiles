# Start from official Postgres docker image  
FROM postgres  
  
# Run additional setup via shell script: create user and db as well as edit
pg_hba.conf  
ADD make_db.sh /docker-entrypoint-initdb.d/

