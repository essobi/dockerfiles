FROM pupudaye/centos-java:latest  
MAINTAINER Waitfish <lipu8829@qq.com>  
ADD apache-tomcat-8.0.47.tar.gz /opt/install  
ADD run.sh /opt/envi/run.sh  
ENV CATALINA_HOME /opt/install/apache-tomcat-8.0.47  
ENV PATH $PATH:$CATALINA_HOME/bin  
RUN chmod 755 /opt/envi/*.sh  
EXPOSE 8080  
CMD ["/opt/envi/run.sh"]  

