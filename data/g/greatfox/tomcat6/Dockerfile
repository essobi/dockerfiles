FROM greatfox/openjre7headless  
MAINTAINER Liang Dong <greatfox@gmail.com>  
  
RUN apt-get -y install tomcat6  
  
RUN echo "/usr/bin/service tomcat6 start\n" >> /initrc  
  
EXPOSE 8080  

