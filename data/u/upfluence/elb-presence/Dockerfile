FROM upfluence/python:latest  
MAINTAINER Alexis Montagne <alexis.montagne@gmail.com>  
  
RUN mkdir -p /opt  
WORKDIR /opt  
  
ADD elb-presence.py /opt/elb-presence.py  
ADD requirements.txt /opt/requirements.txt  
  
RUN pip install -r requirements.txt  
  
CMD etcdenv -n /environments/global -s http://172.17.42.1:4001 \  
python elb-presence.py  
  
RUN rm -rf /tmp/*  

