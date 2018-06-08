# Arch_Flower  
FROM pixeldragon/fedora:24  
MAINTAINER [Andreas Trawoeger <atrawog@hexaplant.com>]  
  
RUN mkdir -p /config /data /log /code  
  
RUN dnf install -y python3-celery python3-flower python3-pytz redis python-pip  
  
RUN pip3 install flower  
  
EXPOSE 5555  
ENV REDIS_HOST redis  
ENV REDIS_PORT 6379  
ENV REDIS_DATABASE 0  
CMD flower --port=5555
--broker=redis://$REDIS_HOST:$REDIS_PORT/$REDIS_DATABASE  

