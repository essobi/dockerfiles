FROM ubuntu:trusty  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && \  
apt-get -y upgrade && \  
apt-get -y install git curl libcurl4-openssl-dev build-essential && \  
apt-get -y install python-dev python-pip python-virtualenv  
  
ADD . /opt/cyclops  
WORKDIR /opt/cyclops  
ENV PYTHONPATH /opt/cyclops  
RUN pip install -r requirements.txt  
  
EXPOSE 9000  
CMD python -m cyclops.server -vv -b 0.0.0.0 -p 9000 -c cyclops.conf  

