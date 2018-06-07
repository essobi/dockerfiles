FROM python:latest  
MAINTAINER huangwc@easecloud.cn  
  
WORKDIR /var/app  
  
ENV PROJECT=app  
ENV WORKERS=1  
ENV WORKER_CLASS=sync  
# or eventlet/greenlet  
RUN apt-get update && apt-get upgrade -y && apt-get autoremove -y  
  
COPY ./startup.sh /var  
COPY ./cron.sh /var  
COPY ./build.sh /var  
COPY ./requirements.txt /var  
  
RUN chmod +x /var/startup.sh && chmod +x /var/build.sh && chmod +x
/var/cron.sh  
RUN /var/build.sh  
  
VOLUME /var/app  
  
EXPOSE 8000  
CMD ["/var/startup.sh"]  
  

