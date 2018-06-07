FROM postgres:9.6  
# Install the postgres python language  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
"postgresql-plpython-$PG_MAJOR" \  
&& apt-get install -y python-pip python-dev  
  
# Install python rsa module for signature verification  
RUN pip install rsa  
  
# Copy all of the SQL scripts into the container  
COPY sql sql  
  
# Copy the shell scripts into the container entry point.  
# These will be run automatically.  
COPY sh /docker-entrypoint-initdb.d  

