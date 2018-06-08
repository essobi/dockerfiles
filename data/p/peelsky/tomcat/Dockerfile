FROM peelsky/zulu-openjdk-busybox  
MAINTAINER Piotr Limanowski <plimanowski@gmail.com>  
  
ENV TOMCAT_VERSION 8.0.17  
RUN (curl -o /tmp/tomcat.zip -L
http://mirror.tcpdiag.net/apache/tomcat/tomcat-${TOMCAT_VERSION:0:1}/v${TOMCAT_VERSION}/bin/apache-
tomcat-${TOMCAT_VERSION}.zip &&\  
unzip -q /tmp/tomcat.zip -d /opt &&\  
rm /opt/apache-tomcat-${TOMCAT_VERSION}/bin/*.bat &&\  
ln -s /opt/apache-tomcat-${TOMCAT_VERSION} /opt/tomcat &&\  
chmod a+x /opt/tomcat/bin/catalina.sh &&\  
ln -s /opt/tomcat/bin/catalina.sh /bin/catalina.sh &&\  
rm /tmp/tomcat.zip)  
  
RUN ln -s /opt/tomcat/webapps /app  
  
ONBUILD EXPOSE 8080  
ONBUILD COPY target/*.war /app/  
ONBUILD WORKDIR /app  
  
ENTRYPOINT ["catalina.sh"]  
CMD ["run"]  

