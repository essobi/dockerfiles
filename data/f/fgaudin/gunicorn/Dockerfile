FROM fgaudin/base:3  
MAINTAINER Francois Gaudin <francois@presencelearning.com>  
  
RUN \  
apt-get update && apt-get install -y build-essential python-dev python-pip \  
&& pip install gunicorn && touch /etc/gunicorn.py  
  
COPY supervisord.conf /etc/supervisor/conf.d/gunicorn.conf  
COPY logstash-forwarder.conf /etc/logstash-forwarder/gunicorn.conf  
  
RUN mkdir -p /opt/app  
WORKDIR /opt/app  
  
EXPOSE 8000  

