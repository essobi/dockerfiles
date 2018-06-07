FROM python:2-alpine  
MAINTAINER Helder Correia <me@heldercorreia.com>  
  
RUN pip install -U docker-cloud  
  
COPY scripts /scripts  
COPY docker-entrypoint.sh /  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD ["crond", "-f", "-d", "8"]  

