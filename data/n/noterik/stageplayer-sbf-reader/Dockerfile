FROM openjdk:8-jdk as builder  
# Installs Ant  
ENV ANT_VERSION 1.9.4  
RUN cd && \  
wget -q http://archive.apache.org/dist/ant/binaries/apache-
ant-${ANT_VERSION}-bin.tar.gz && \  
tar -xzf apache-ant-${ANT_VERSION}-bin.tar.gz && \  
mv apache-ant-${ANT_VERSION} /opt/ant && \  
rm apache-ant-${ANT_VERSION}-bin.tar.gz  
  
ENV ANT_HOME /opt/ant  
ENV PATH ${PATH}:/opt/ant/bin  
  
# COPY OVER JAVA CODE TO DOCKER CONTAINER  
COPY src /home/stageplayer-sbf-reader/src/  
COPY libs /home/stageplayer-sbf-reader/libs/  
COPY WebContent /home/stageplayer-sbf-reader/WebContent/  
COPY /build.xml /home/stageplayer-sbf-reader/  
  
RUN cd /home/stageplayer-sbf-reader && ant  
  
FROM tomcat:6.0.53-jre8  
  
ENV CATALINA_HOME /usr/local/tomcat  
  
#COPY TOMCAT DEPENDENCIES  
COPY /docker-libs/tomcat-users.xml $CATALINA_HOME/conf/tomcat-users.xml  
COPY /docker-libs/log4j-1.2.15.jar $CATALINA_HOME/lib/log4j-1.2.15.jar  
COPY /docker-libs/log4j.properties $CATALINA_HOME/lib/log4j.properties  
COPY /docker-libs/tomcat-juli-adapters.jar $CATALINA_HOME/lib/tomcat-juli-
adapters.jar  
COPY /docker-libs/javax.json-1.0.4.jar $CATALINA_HOME/lib/javax.json-1.0.4.jar  
COPY /docker-libs/tomcat-juli.jar $CATALINA_HOME/bin/tomcat-juli.jar  
  
COPY \--from=builder /home/stageplayer-sbf-reader/war/stageplayer-sbf-
reader.war $CATALINA_HOME/webapps/  
  
# TODO find a simple hacky way to verify Tomcat Native is working properly  
# (the way we use in 7+ doesn't work here because we have no "configtest")  
RUN rm $CATALINA_HOME/conf/logging.properties  
  
EXPOSE 8080  
CMD ["catalina.sh", "run"]

