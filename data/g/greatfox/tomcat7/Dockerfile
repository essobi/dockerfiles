FROM greatfox/openjre7headless  
MAINTAINER Liang Dong <greatfox@gmail.com>  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install tomcat7  
  
RUN echo "/usr/bin/service tomcat7 start\n" >> /initrc  
  
EXPOSE 8080  

