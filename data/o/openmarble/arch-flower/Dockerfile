# Arch_Flower  
FROM openmarble/arch-vips:latest  
MAINTAINER Andreas Trawöger <atrawog@openmarble.org>  
  
RUN sudo pip install --upgrade redis && \  
sudo pip install --upgrade celery && \  
sudo pip install --upgrade flower  
  
EXPOSE 5555  
ENV REDIS_HOST redis  
ENV REDIS_PORT 6379  
ENV REDIS_DATABASE 0  
CMD flower --port=5555
--broker=redis://$REDIS_HOST:$REDIS_PORT/$REDIS_DATABASE

