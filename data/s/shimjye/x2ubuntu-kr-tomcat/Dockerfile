FROM shimjye/x2ubuntu-kr  
LABEL maintainer="shimjye@gmail.com"  
  
RUN apt-get update  
RUN apt-get install -y openjdk-8-jre  
  
# tomcat  
ENV TOMCAT_MAJOR_VERSION 9  
ENV TOMCAT_MINOR_VERSION 9.0.1  
RUN wget -q
https://archive.apache.org/dist/tomcat/tomcat-${TOMCAT_MAJOR_VERSION}/v${TOMCAT_MINOR_VERSION}/bin/apache-
tomcat-${TOMCAT_MINOR_VERSION}.tar.gz && \  
wget -qO-
https://archive.apache.org/dist/tomcat/tomcat-${TOMCAT_MAJOR_VERSION}/v${TOMCAT_MINOR_VERSION}/bin/apache-
tomcat-${TOMCAT_MINOR_VERSION}.tar.gz.md5 | md5sum -c - && \  
tar zxf apache-tomcat-*.tar.gz && \  
rm apache-tomcat-*.tar.gz && \  
mv apache-tomcat* /opt/tomcat && \  
chown -R 1000:1000 /opt/tomcat  
  
EXPOSE 22 8080  
CMD ["/run.sh"]  

