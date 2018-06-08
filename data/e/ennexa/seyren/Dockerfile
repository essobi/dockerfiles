FROM java:openjdk-8-jre-alpine  
MAINTAINER Usman Ismail "usman@techtraits.com"  
ADD https://github.com/scobal/seyren/releases/download/1.4.0/seyren-
web-1.4.0.jar /opt/seyren.jar  
ADD run-seyren.sh /usr/bin/run-seyren.sh  
RUN chmod +x /usr/bin/run-seyren.sh  
  
ENTRYPOINT ["/usr/bin/run-seyren.sh"]  
EXPOSE 8080  

