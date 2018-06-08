FROM webcenter/openjdk-jre  
  
MAINTAINER Ritu Singh & Jones Alapat  
  
ADD target/WeatherMicroService-1.0.jar /opt  
ADD ./run_microservice.sh /opt/run_microservice.sh  
  
RUN chmod 777 /opt/WeatherMicroService-1.0.jar  
  
EXPOSE 9003  
CMD ["/bin/sh", "-e", "/opt/run_microservice.sh"]  
  

