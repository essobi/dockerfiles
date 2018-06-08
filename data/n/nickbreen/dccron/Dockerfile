FROM nickbreen/cron:v1.0.0  
  
MAINTAINER Nick Breen <nick@foobarnet.nz>  
  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -qqy
python-pip jq && apt-get clean  
  
RUN pip install python-dockercloud  
  
ENV DOCKERCLOUD_USER="" DOCKERCLOUD_APIKEY=""  
  
COPY run /etc/service/dccron/run  
  
COPY dccron.py /opt/dccron/  

