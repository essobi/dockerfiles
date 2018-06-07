FROM quay.io/lizhongwen/oracle-jdk:1.7  
MAINTAINER github.com/Official-Registry, lizhongwen1989@gmail.com  
  
#  
# http://www.eclipse.org/jetty/download.html  
#  
ENV JETTY_VERSION=8.1.19.v20160209  
ENV JETTY_HOME=/opt/app/jetty  
ENV JAVA_DEBUG=false  
ENV JVM_MIN_MEM=256  
ENV JVM_MAX_MEM=1024  
EXPOSE 8080 8888  
RUN curl --fail --location --retry 3 \  
http://repo1.maven.org/maven2/org/eclipse/jetty/jetty-
distribution/8.1.19.v20160209/jetty-distribution-8.1.19.v20160209.tar.gz \  
-o /tmp/jetty.tar.gz \  
&& tar -zvxf /tmp/jetty.tar.gz -C /tmp/ \  
&& mkdir -p /opt/app/ \  
&& mv /tmp/jetty-distribution-${JETTY_VERSION} ${JETTY_HOME} \  
&& rm -rf /tmp/jetty.tar.gz ${JETTY_HOME}/webapps/*.war
${JETTY_HOME}/contexts/* ${JETTY_HOME}/contexts-available/*
${JETTY_HOME}/javadoc  
  
ADD resources/entrypoint.sh ${JETTY_HOME}/bin/  
  
RUN chmod +x ${JETTY_HOME}/bin/entrypoint.sh \  
&& apt-get install -y unzip  
  
ENTRYPOINT ["/bin/sh", "-c", "${JETTY_HOME}/bin/entrypoint.sh"]  

