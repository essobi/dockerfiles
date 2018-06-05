#  
# Docker image for BEAST Alarm Server's PostgreSQL.  
#  
# Author: Gustavo Ciotto Pinton  
# Controls Group - Brazilian Synchrotron Light Source Laboratory - LNLS  
#  
FROM postgres:latest  
  
MAINTAINER Gustavo Ciotto  
  
# According to the documentation, all sql files are executed when the
container  
# is started.  
COPY sql/*.sql /docker-entrypoint-initdb.d/  
  
CMD ["postgres"]  

