FROM jboss/base-jdk:8  
MAINTAINER Gary Brown <gbrown@redhat.com>  
LABEL io.k8s.description="Hawkular APM Server is an application monitoring
solution" \  
io.k8s.display-name="Hawkular APM Server" \  
io.openshift.tags="hawkular,apm,opentracing" \  
io.openshift.expose-services="8080:http" \  
io.openshift.s2i.scripts-url=image:///usr/libexec/s2i  
  
# Labels consumed by Red Hat build service  
LABEL com.redhat.component="openshift-hawkular-apm-docker" \  
name="openshift3/hawkular-apm-server-rhel7" \  
version="0.14.4.Final" \  
architecture="x86_64" \  
release="7"  
  
USER jboss  
  
ENV HAWKULAR_APM_VERSION 0.14.4.Final  
ENV JBOSS_HOME /opt/jboss/hawkular-apm-server  
  
# Download Hawkular-APM from github  
RUN cd $HOME \  
&& curl -O -L https://github.com/hawkular/hawkular-
apm/releases/download/$HAWKULAR_APM_VERSION/hawkular-apm-
dist-$HAWKULAR_APM_VERSION.zip \  
&& unzip -d $JBOSS_HOME hawkular-apm-dist-$HAWKULAR_APM_VERSION.zip \  
&& rm hawkular-apm-dist-$HAWKULAR_APM_VERSION.zip  
  
ADD standalone-wrapper.sh /opt/jboss/hawkular-apm-server/bin/standalone-
wrapper.sh  
  
# Ensure signals are forwarded to the JVM process correctly for graceful
shutdown  
ENV LAUNCH_JBOSS_IN_BACKGROUND true  
  
# Expose the ports we're interested in  
EXPOSE 8080  
#### openshift hack: figure out the proper way to deal with this  
USER root  
RUN chgrp 0 /opt/jboss -R && chmod g+rw /opt/jboss -R  
USER jboss  
  
# Set the default command to run on boot  
# This will boot Hawkular and bind to all interface  
CMD ["/opt/jboss/hawkular-apm-server/bin/standalone-
wrapper.sh","-b","0.0.0.0","-bmanagement","0.0.0.0"]  

