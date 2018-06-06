FROM python:latest  
MAINTAINER Stale Pettersen  
RUN apt-get update && apt-get install -y jq mongodb-clients  
RUN pip install 'mongo-connector[elastic2]'  
COPY scripts /data  
WORKDIR /data  
CMD bash /data/run.sh  

