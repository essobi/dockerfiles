FROM greatfox/oraclejdk8  
MAINTAINER Liang Dong <greatfox@gmail.com>  
  
RUN wget -qO /dev/stdout
https://www.apache.org/dist/tomcat/tomcat-8/v8.0.18/bin/apache-
tomcat-8.0.18.tar.gz | tar zxv -C /opt/  
RUN ln -s /opt/apache-tomcat-8* /opt/tomcat8  
RUN useradd -d /opt/tomcat8 -s /bin/false -M -U tomcat8  
RUN chown -R tomcat8:tomcat8 /opt/tomcat8 /opt/apache-tomcat-8*  
RUN echo 'sudo -u tomcat8 /opt/tomcat8/bin/startup.sh' >> /initrc  
  

