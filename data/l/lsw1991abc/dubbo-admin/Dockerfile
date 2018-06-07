FROM tomcat:8.5  
LABEL maintainer="lsw1991abc@gmail.com"  
  
ARG DISTRO_NAME=dubbo-admin-2.5.5  
ENV TOMCAT_HOME=/usr/local/tomcat \  
PROPERTIES=/usr/local/tomcat/webapps/ROOT/WEB-INF/dubbo.properties  
  
RUN rm -rf $TOMCAT_HOME/webapps/*  
RUN wget -P /opt/
https://github.com/lsw1991abc/uploads/archive/$DISTRO_NAME.tar.gz  
RUN tar -zxf /opt/$DISTRO_NAME.tar.gz -C $TOMCAT_HOME/webapps  
RUN mv $TOMCAT_HOME/webapps/uploads-$DISTRO_NAME $TOMCAT_HOME/webapps/ROOT &&
rm /opt/$DISTRO_NAME.tar.gz && rm $PROPERTIES  
  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD ["bin/catalina.sh", "run"]  

