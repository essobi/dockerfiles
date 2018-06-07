FROM liling/phusion-java:jdk7  
  
MAINTAINER liling@bit.edu.cn  
  
EXPOSE 8080  
ENV JETTY_VERSION 8.1.21.v20160908  
ENV JETTY_HOME /opt/jetty  
ENV DEPLOY_DIR /opt/deploy  
ENV OPENSHIFT_DATA_DIR /opt/deploy/data  
  
# Unpack and delete demo files  
RUN cd /opt && wget http://central.maven.org/maven2/org/eclipse/jetty/jetty-
distribution/${JETTY_VERSION}/jetty-distribution-${JETTY_VERSION}.tar.gz -O -
| tar zxf - --exclude=javadoc --exclude=contexts-available
--exclude='contexts' \--exclude='webapps' ; mv /opt/jetty-
distribution-${JETTY_VERSION} ${JETTY_HOME} ; chown root.root ${JETTY_HOME} -R
; sed -i -e 's/GMT/Asia\/Shanghai/' $JETTY_HOME/etc/jetty-logging.xml  
  
# Startup script  
ADD deploy-and-run.sh /opt/jetty/bin/  
  
WORKDIR /opt/jetty  
  
ENV LC_ALL zh_CN.UTF-8  
CMD /opt/jetty/bin/deploy-and-run.sh  

