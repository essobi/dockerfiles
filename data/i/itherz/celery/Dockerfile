FROM python:3.6-slim  
  
WORKDIR /opt/module  
  
ENV CELERY_VERSION 4.0.2  
RUN pip install celery=="$CELERY_VERSION"  
  
ENV CELERY_BROKER_URL amqp://guest@rabbit  
  
ENV C_FORCE_ROOT=true  
  
RUN echo "deb http://mirror.yandex.ru/debian/ stable main contrib non-free"
>/etc/apt/sources.list && apt update -y && apt install -y git && rm -rf
/var/cache/apt/*  
  
CMD [ "celery", "worker" ]  

