FROM tomcat:8.5-jre8-alpine  
  
ENV AXIS2_VERSION=1.7.7 \  
AXIS2_INSTALL_DIR=/usr/local/axis2 \  
AXIS2_SERVICES_DIR=/usr/local/axis2/WEB-INF/services  
  
WORKDIR /tmp  
COPY config/server.xml /usr/local/tomcat/conf/server.xml  
COPY config/axis2.xml /usr/local/tomcat/conf/Catalina/localhost/axis2.xml  
RUN mkdir ${AXIS2_INSTALL_DIR} && \  
cd ${AXIS2_INSTALL_DIR} && \  
wget http://www-
eu.apache.org/dist/axis/axis2/java/core/${AXIS2_VERSION}/axis2-${AXIS2_VERSION}-war.zip
&& \  
unzip axis2-${AXIS2_VERSION}-war.zip && \  
unzip axis2.war && \  
rm -rf axis2-${AXIS2_VERSION}-war.zip axis2.war *.txt

