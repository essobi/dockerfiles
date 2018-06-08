FROM develar/java:latest  
  
RUN apk --update add pwgen ca-certificates libssl1.0 libuuid openssl apr
libcrypto1.0 && \  
rm -rf /tmp/* /var/cache/apk/*  
  
ENV TOMCAT_MAJOR_VERSION 8  
ENV TOMCAT_MINOR_VERSION 8.5.24  
ENV CATALINA_HOME /tomcat  
ENV CATALINA_TMPDIR /tmp  
  
# INSTALL TOMCAT  
RUN wget -q
https://archive.apache.org/dist/tomcat/tomcat-${TOMCAT_MAJOR_VERSION}/v${TOMCAT_MINOR_VERSION}/bin/apache-
tomcat-${TOMCAT_MINOR_VERSION}.tar.gz && \  
wget -qO-
https://archive.apache.org/dist/tomcat/tomcat-${TOMCAT_MAJOR_VERSION}/v${TOMCAT_MINOR_VERSION}/bin/apache-
tomcat-${TOMCAT_MINOR_VERSION}.tar.gz.md5 | md5sum -c - && \  
tar zxf apache-tomcat-*.tar.gz && \  
rm apache-tomcat-*.tar.gz && \  
mv apache-tomcat* tomcat && \  
rm -rf /tomcat/webapps/examples /tomcat/webapps/docs /tomcat/webapps/ROOT  
  
ADD create_tomcat_admin_user.sh /create_tomcat_admin_user.sh  
ADD run.sh /run.sh  
ADD server.xml /tomcat/conf/server.xml  
RUN chmod +x /*.sh  
  
EXPOSE 8080  
VOLUME /tomcat/logs  
# reset entrypoint from parent image  
ENTRYPOINT []  
CMD ["/run.sh"]  

