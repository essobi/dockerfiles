FROM openjdk:8  
ENV VERSION 7.0.3  
ENV ARCHIVE apache-tomee-$VERSION-webprofile  
  
ENV INSTALL_DIR=""  
ENV SERVER_HOME ${INSTALL_DIR}/${ARCHIVE}  
  
ENV DEPLOYMENT_DIR ${SERVER_HOME}/webapps/  
  
RUN curl -o ${SERVER_HOME}.zip -L
http://repo.maven.apache.org/maven2/org/apache/tomee/apache-
tomee/$VERSION/$ARCHIVE.zip
http://repo.maven.apache.org/maven2/org/apache/tomee/apache-
tomee/$VERSION/${ARCHIVE} \  
&& unzip ${SERVER_HOME}.zip -d /$INSTALL_DIR \  
&& rm ${SERVER_HOME}.zip && mv $(ls -d apache-tomee-webprofile*)
${INSTALL_DIR}/${ARCHIVE}  
  
ENTRYPOINT ${SERVER_HOME}/bin/catalina.sh run  
  
EXPOSE 8080  

