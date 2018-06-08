FROM debian:latest  
MAINTAINER Laureano Fernandez <laureano.fernandez@nitelmursoftware.es>  
  
ENV DEVICE name  
ENV PASSWORD pass  
  
COPY install.sh /  
#debdir is a directory  
COPY debdir /debdir  
RUN chmod +x /install.sh  
  
CMD ["/install.sh"]  
EXPOSE 5000 5314  

