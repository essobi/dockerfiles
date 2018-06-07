FROM learninglayers/base  
MAINTAINER Gordon Lawrenz <lawrenz@dbis.rwth-aachen.de>  
  
# Install Java.  
RUN apt-get update && apt-get install -yq software-properties-common  
ADD src/main/files/init.sh /opt/init.sh  
ADD src/main/files/init /opt/init  
RUN chmod +x /opt/init.sh \  
&& chmod -R +x /opt/init  
RUN \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y oracle-java8-installer && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/oracle-jdk8-installer  
  
# Define working directory.  
WORKDIR /data  
  
# Define commonly used JAVA_HOME variable  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
  
# Define default command.  
CMD ["bash"]  
  
ENV TOMCAT_HOME="/opt/tomcat"  
ENV PATH=$JAVA_HOME/bin:$TOMCAT_HOME/bin:$PATH  
  
ENV TOMCAT_MINOR_VERSION 8.5.9  
ENV CATALINA_HOME /opt/tomcat  
  
RUN curl -O
http://archive.apache.org/dist/tomcat/tomcat-8/v${TOMCAT_MINOR_VERSION}/bin/apache-
tomcat-${TOMCAT_MINOR_VERSION}.tar.gz && \  
curl
http://archive.apache.org/dist/tomcat/tomcat-8/v${TOMCAT_MINOR_VERSION}/bin/apache-
tomcat-${TOMCAT_MINOR_VERSION}.tar.gz.md5 | md5sum -c - && \  
gunzip apache-tomcat-*.tar.gz && \  
tar xf apache-tomcat-*.tar && \  
rm apache-tomcat-*.tar && mv apache-tomcat* ${CATALINA_HOME} && \  
rm -rf ${CATALINA_HOME}/webapps/examples \  
${CATALINA_HOME}/webapps/docs ${CATALINA_HOME}/webapps/ROOT \  
${CATALINA_HOME}/webapps/host-manager \  
${CATALINA_HOME}/RELEASE-NOTES ${CATALINA_HOME}/RUNNING.txt \  
${CATALINA_HOME}/bin/*.bat ${CATALINA_HOME}/bin/*.tar.gz  
  
WORKDIR /opt/tomcat  
EXPOSE 8080  
VOLUME [ "/opt/tomcat", "/opt", "opt/init" ]  
  
ENTRYPOINT [ "/opt/init.sh" ]  
CMD [ "run"]  

