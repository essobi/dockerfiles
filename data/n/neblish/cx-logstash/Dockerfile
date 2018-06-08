FROM logstash:latest  
MAINTAINER Benjamin Lai <theneb.bstl@gmail.com>  
  
#Copy all configurations into the image  
COPY ./config/*.conf /etc/logstash/conf.d/  
  
#Expose Port 5000 for Beats and 5044 for TCP  
EXPOSE 5000 5044  

