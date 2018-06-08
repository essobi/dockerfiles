#  
# Copyright (c) 2001-2018 Primeton Technologies, Ltd.  
# All rights reserved.  
#  
# author: ZhongWen Li (mailto:lizw@primeton.com)  
#  
FROM primetoninc/jdk:latest  
  
# LABEL maintainer="lizw@primeton.com" \  
# provider="Primeton Technologies, Ltd."  
ENV TOMCAT_VERSION="7.0.81"  
# ENV TOMCAT_HOME="/opt/apache-tomcat-${TOMCAT_VERSION}"  
ENV TOMCAT_HOME="/tomcat"  
# YES | NO  
ENV JAVA_DEBUG=NO \  
JAVA_VM_MEM_MIN=512 \  
JAVA_VM_MEM_MAX=1024 \  
TOMCAT_MAX_THREADS=10000 \  
TOMCAT_MIN_SEPARE_THREADS=10  
# tomcat: 8080  
# debug: 8888  
EXPOSE 8080 8888  
RUN curl --fail --location --retry 3 \  
https://archive.apache.org/dist/tomcat/tomcat-7/v7.0.81/bin/apache-
tomcat-7.0.81.tar.gz \  
-o /tmp/tomcat.tar.gz \  
&& tar -zvxf /tmp/tomcat.tar.gz -C /tmp/ \  
&& \mv -f /tmp/apache-tomcat* ${TOMCAT_HOME} \  
&& mkdir -p ${TOMCAT_HOME}/backup \  
&& \mv -f ${TOMCAT_HOME}/webapps/ROOT ${TOMCAT_HOME}/backup/ \  
&& \rm -rf /tmp/tomcat.tar.gz ${TOMCAT_HOME}/webapps/*  
  
# Inject tomcat ThreadPool size by environment on docker run  
ADD resources/server.xml ${TOMCAT_HOME}/conf/server-template.xml  
  
ADD resources/entrypoint.sh ${TOMCAT_HOME}/bin/  
  
RUN chmod +x ${TOMCAT_HOME}/bin/entrypoint.sh  
  
ENTRYPOINT [ "/bin/sh", "-c", "${TOMCAT_HOME}/bin/entrypoint.sh" ]  

