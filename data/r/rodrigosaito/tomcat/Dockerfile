FROM rodrigosaito/java:8  
ENV TOMCAT_BASE_PATH /usr/lib  
ENV TOMCAT_HOME ${TOMCAT_BASE_PATH}/tomcat  
ENV TOMCAT_VERSION_MAJOR 7  
ENV TOMCAT_VERSION_FULL 7.0.67  
ENV PATH ${PATH}:${TOMCAT_HOME}/bin  
  
RUN apk --update --virtual=build-dependencies add curl ca-certificates tar \  
&& mkdir -p $TOMCAT_BASE_PATH \  
&& curl -Ls
http://apache.mirrors.hoobly.com/tomcat/tomcat-$TOMCAT_VERSION_MAJOR/v$TOMCAT_VERSION_FULL/bin/apache-
tomcat-$TOMCAT_VERSION_FULL.tar.gz | tar -xzf - -C $TOMCAT_BASE_PATH \  
&& ln -s $TOMCAT_BASE_PATH/apache-tomcat-$TOMCAT_VERSION_FULL $TOMCAT_HOME \  
&& addgroup -S tomcat && adduser -S -G tomcat -h $TOMCAT_HOME -s /sbin/nologin
tomcat \  
&& chown -R tomcat:tomcat $TOMCAT_BASE_PATH/apache-tomcat-$TOMCAT_VERSION_FULL
\  
&& rm -rf $TOMCAT_HOME/webapps/* \  
&& apk del build-dependencies  
  
USER tomcat  
  
WORKDIR $TOMCAT_HOME  
  
EXPOSE 8080  
CMD [ "catalina.sh", "run" ]  

