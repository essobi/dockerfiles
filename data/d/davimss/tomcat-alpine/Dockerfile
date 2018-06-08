FROM openjdk:7-jdk-alpine  
  
USER root  
  
ENV TOMCAT_MAJOR 7  
ENV TOMCAT_VERSION 7.0.59  
ENV TOMCAT_DIR apache-tomcat-$TOMCAT_VERSION  
ENV TOMCAT_DOWN_FILE $TOMCAT_DIR.tar.gz  
ENV CATALINA_HOME /opt/$TOMCAT_DIR  
ENV PATH $CATALINA_HOME/bin:$PATH  
  
WORKDIR /opt  
  
RUN set -x ; \  
wget
http://archive.apache.org/dist/tomcat/tomcat-$TOMCAT_MAJOR/v$TOMCAT_VERSION/bin/$TOMCAT_DOWN_FILE
; \  
tar -xvf $TOMCAT_DOWN_FILE ; \  
rm -rf $CATALINA_HOME/bin/*.bat ; \  
rm -rf $TOMCAT_DOWN_FILE ; \  
rm -rf $CATALINA_HOME/webapps/docs ; \  
rm -rf $CATALINA_HOME/webapps/examples ; \  
ln -s $CATALINA_HOME /opt/tomcat  
  
WORKDIR $CATALINA_HOME  
COPY setenv.sh bin/setenv.sh  
#COPY server.xml conf/server.xml  
COPY tomcat-users.xml conf/tomcat-users.xml  
COPY logging.properties conf/logging.properties  
  
# Volume nomeado deve ser declarado no momento de criar o container, com o  
# parametro "-v nome-do-volume:/opt/apache-tomcat-7.0.59/logs" e nao aqui no
Dockerfile  
# ver https://boxboat.com/2017/01/23/volumes-and-dockerfiles-dont-mix/  
#VOLUME "$CATALINA_HOME/logs"  
EXPOSE 8080  
CMD ["catalina.sh", "run"]

