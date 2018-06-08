FROM alpine:3.4  
RUN apk add --update openjdk7 && \  
cd /root && \  
wget
http://apache.mirrors.ovh.net/ftp.apache.org/dist/tomcat/tomcat-8/v8.5.6/bin/apache-
tomcat-8.5.6.tar.gz && \  
mkdir /opt && \  
cd /opt && \  
tar xf /root/apache-tomcat-8.5.6.tar.gz && \  
cd /opt/apache-tomcat-8.5.6/webapps && \  
mkdir dom && \  
cd dom && \  
rm -f /root/apache-tomcat-8.5.6.tar.gz  
  
COPY index.html /opt/apache-tomcat-8.5.6/webapps/dom  
  
CMD ["/opt/apache-tomcat-8.5.6/bin/catalina.sh","run"]  

