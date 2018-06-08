## -*- docker-image-name: "mcreations/openwrt-tomcat" -*-  
FROM mcreations/openwrt-java:8  
MAINTAINER Reza Rahimi <rahimi@m-creations.net>  
  
ENV TOMCAT_VERSION=8.5.5  
ENV CATALINA_HOME /opt/apache-tomcat-${TOMCAT_VERSION}  
  
ADD image/root /  
  
ENV MAX_THREADS 200  
ENV MAX_CONNECTIONS 1000  
ENV ACCEPT_COUNT 100  
ENV MIN_SPARE_THREADS 100  
ENV JVM_ARG_XMS 128m  
ENV JVM_ARG_XMX 256m  
ENV JVM_ARG_XSS 128m  
  
#To use jconsole In Mesos env for example on server: mesos-server-
name.example.com  
# 1) ssh with prot forewarding from the client to the mesos-server  
# ssh -L 6970:localhost:6970 root@mesos-server-name.example.com  
# 2) Add following parameters to docker run:  
# -p 6970:6970 \  
# -e JAVA_RMI_SERVER_HOSTNAME=mesos-server-name.example.com  
# 3) Run jconsole from the client which use ssh port forwarding  
# jconsole localhost:6970  
#  
ENV JMX_PORT 6970  
EXPOSE 6970  
ENV JPDA_ADDRESS=8000  
# y for yes or n for no  
ENV JPDA_SUSPEND=n  
ENV JPDA_TRANSPORT=dt_socket  
#ENV JPDA_XDEBUG_OPTS="-Xdebug
-Xrunjdwp:transport=dt_socket,address=$JPDA_ADDRESS,server=y,suspend=${JPDA_SUSPEND}"  
ENV JPDA_START=false  
EXPOSE $JPDA_ADDRESS  
  
# Download TOMCAT and installing it  
RUN opkg update && \  
opkg install libapr libaprutil && \  
export TOMCAT_MAJOR_VERSION=`echo "$TOMCAT_VERSION" | cut -d. -f1` && \  
wget -O /tmp/apache-tomcat-${TOMCAT_VERSION}.tar.gz --progress=dot:giga
https://archive.apache.org/dist/tomcat/tomcat-${TOMCAT_MAJOR_VERSION}/v${TOMCAT_VERSION}/bin/apache-
tomcat-${TOMCAT_VERSION}.tar.gz && \  
tar -C /tmp -xvzf /tmp/apache-tomcat-${TOMCAT_VERSION}.tar.gz && \  
rm /tmp/apache-tomcat-${TOMCAT_VERSION}.tar.gz && \  
mv -f /tmp/apache-tomcat-${TOMCAT_VERSION} ${CATALINA_HOME} && \  
rm -f ${CATALINA_HOME}/bin/*.bat && \  
rm -r ${CATALINA_HOME}/webapps/examples && \  
rm -r ${CATALINA_HOME}/webapps/docs && \  
rm -r ${CATALINA_HOME}/webapps/manager && \  
rm -r ${CATALINA_HOME}/webapps/host-manager && \  
echo "export PATH=$PATH:$JAVA_HOME/bin/bundled:${CATALINA_HOME}/bin" >>
/etc/profile && \  
echo "export CATALINA_HOME=${CATALINA_HOME}" >> /etc/profile  
  
# Expose port  
EXPOSE 8080  
CMD ["/start-tomcat"]  

