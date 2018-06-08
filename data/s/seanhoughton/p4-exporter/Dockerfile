FROM python:3.6  
MAINTAINER Sean Houghton <sean.houghton@activision.com>  
  
COPY requirements.txt /tmp/requirements.txt  
RUN pip install -r /tmp/requirements.txt && rm /tmp/requirements.txt  
  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
RUN chmod +x /docker-entrypoint.sh  
  
COPY p4exporter.py /usr/bin/p4exporter.py  
RUN chmod +x /usr/bin/p4exporter.py  
  
EXPOSE 9666  
ENTRYPOINT ["/docker-entrypoint.sh"]

