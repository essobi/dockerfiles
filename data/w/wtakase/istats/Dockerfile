FROM python:2.7  
MAINTAINER wtakase <wataru.takase@kek.jp>  
  
RUN apt-get update && apt-get install -y cron  
RUN pip install git+git://github.com/irods/python-irodsclient.git  
RUN mkdir -p /opt/istats/log && \  
touch /opt/istats/log/istats.log && \  
touch /opt/istats/log/istats_demo.log  
COPY istats/etc /opt/istats/etc/  
COPY istats/bin /opt/istats/bin/  
RUN echo "*/10 * * * * root /opt/istats/bin/istats" >> /etc/crontab  
  
COPY run.sh /  
CMD ["/run.sh"]  

