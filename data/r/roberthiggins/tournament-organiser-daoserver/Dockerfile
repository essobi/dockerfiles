# This will fire up the daoserver. It is a flask app on ubuntu  
# The daoserver is the (eventually) public api server for operations on
players  
# and tournaments. In the mean time it is intended to be run privately; user  
# authentication and permissions are only being added now.  
FROM python:2.7  
MAINTAINER Robert Higgins <robert.h.higgins@gmail.com>  
  
# We need to attach to the database. Docker suggests that normally you  
# shouldn't run update manually. However it is the only way to get  
# python-dev or postgresql to install  
RUN apt-get update && apt-get install -y postgresql libpq-dev  
  
ADD ./requirements.txt ./requirements.txt  
RUN pip install -r requirements.txt  
  
# Add the source dir  
ADD src/ webapp/  
ADD bash_aliases /root/.bash_aliases  
  
# Config  
WORKDIR webapp/  
  
# Add a script to allow waiting for the db  
ADD ./wait-for-postgres.sh ./wait-for-postgres.sh  
  
HEALTHCHECK \--interval=1s --timeout=1s \  
CMD curl --fail http://localhost:5000/ || exit 1  
  
CMD ./wait-for-postgres.sh database python -u app.py  

