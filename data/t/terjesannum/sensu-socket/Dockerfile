FROM terjesannum/sensu-base:2  
LABEL maintainer "terje@offpiste.org"  
  
EXPOSE 3030  
ENV LOG_LEVEL=info  
  
ENV RABBITMQ_HOST=rabbitmq  
ENV RABBITMQ_PORT=5672  
ENV RABBITMQ_VHOST=/  
ENV RABBITMQ_USER=guest  
ENV RABBITMQ_PASSWORD=guest  
  
COPY run.sh /opt/  
CMD ["/opt/run.sh"]  

