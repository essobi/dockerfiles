FROM postgres:9.5.10  
# Add the entrypoint shell script to trigger the database install  
COPY *.sh /docker-entrypoint-initdb.d/  
  
# Create a new directory to hold all the sql init scripts  
RUN mkdir /sql_scripts  
  
# Copy over all sql scripts to the new folder  
COPY / /sql_scripts/

