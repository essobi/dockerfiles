FROM liling/phusion-java:jdk7  
MAINTAINER liling@bit.edu.cn  
  
# Setup jetty  
EXPOSE 8080  
ENV LC_ALL zh_CN.UTF-8  
ENV JETTY_VERSION 9.2.22.v20170606  
ENV JETTY_HOME /opt/jetty-distribution-${JETTY_VERSION}  
ENV JETTY_BASE /opt/jetty-base  
ENV OPENSHIFT_DATA_DIR /opt/deploy/data  
  
# Unpack  
RUN cd /opt && wget http://central.maven.org/maven2/org/eclipse/jetty/jetty-
distribution/${JETTY_VERSION}/jetty-distribution-${JETTY_VERSION}.tar.gz -O -
| tar zxf - ; \  
sed -i -e 's/GMT/Asia\/Shanghai/' $JETTY_HOME/etc/jetty-logging.xml  
  
# Startup script  
ADD deploy-and-run.sh /  
RUN chmod a+x /*.sh  
RUN mkdir /opt/jetty-base  
  
# Final  
ENV PATH $PATH:$JETTY_HOME/bin  
WORKDIR /opt/jetty-base  
CMD /deploy-and-run.sh  

