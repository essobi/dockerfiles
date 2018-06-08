FROM python:2-alpine  
MAINTAINER Victor M. Varela <victor@geographica.gs>  
  
ADD https://github.com/CartoDB/cdb-manager/archive/master.zip .  
RUN unzip master.zip  
WORKDIR ./cdb-manager-master  
  
EXPOSE 8000  
CMD ["python", "./httpserv.py"]  

