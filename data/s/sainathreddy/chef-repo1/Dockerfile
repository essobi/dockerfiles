FROM centos  
MAINTAINER sai  
RUN yum -y install httpd && \  
yum -y install java && \  
yum -y install wget && \  
yum -y install tomcat  
  
RUN echo "hellow httpd file " > /var/www/html/index.html  
  
#RUN wget
http://redrockdigimark.com/apachemirror/tomcat/tomcat-9/v9.0.1/bin/apache-
tomcat-9.0.1.tar.gz  
#RUN tar -xzf apache-tomcat-9.0.1.tar.gz  
#EXPOSE 8080  
EXPOSE 80  
#ENV CATALINA_HOME /apache-tomcat-9.0.1  
#ENV PATH $CATALINA_HOME/bin:$PATH  
WORKDIR /tmp  
  
#CMD ["./startup.sh", "run"]  
EXPOSE 8080  
ONBUILD ADD demo.html /tmp  

