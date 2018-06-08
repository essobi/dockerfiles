# grails  
FROM openshift/base-centos7  
  
EXPOSE 8080  
EXPOSE 8778  
MAINTAINER Patrick Tescher <patrickt@ticketfly.com>  
  
LABEL io.k8s.description="Platform for grails apps" \  
io.k8s.display-name="grails" \  
io.openshift.expose-services="8080:http,8778:jolokia" \  
io.openshift.tags="builder,grails" \  
io.openshift.s2i.destination="/opt/s2i/destination"  
  
RUN yum install -y java-1.6.0-openjdk-devel mysql && yum clean all -y  
ENV JAVA_HOME="/usr/lib/jvm/java-openjdk"  
COPY ./s2i/bin/ $STI_SCRIPTS_PATH  
  
RUN mkdir -p /opt/s2i/destination && chmod -R g+rw /opt/s2i/destination  
  
USER 1001  
CMD $STI_SCRIPTS_PATH/usage  

