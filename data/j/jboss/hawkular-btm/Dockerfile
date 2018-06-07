FROM jboss/base-jdk:8  
MAINTAINER Gary Brown <gbrown@redhat.com>  
  
ENV HAWKULAR_BTM_VERSION 0.8.0.Final  
ENV JBOSS_HOME /opt/jboss/hawkular-btm  
  
# Download Hawkular-BTM from repository.jboss.org  
RUN cd $HOME \  
&& curl -O
https://repository.jboss.org/nexus/service/local/repositories/central/content/org/hawkular/btm/hawkular-
btm-dist/$HAWKULAR_BTM_VERSION/hawkular-btm-dist-$HAWKULAR_BTM_VERSION.zip \  
&& unzip -d $JBOSS_HOME hawkular-btm-dist-$HAWKULAR_BTM_VERSION.zip \  
&& rm hawkular-btm-dist-$HAWKULAR_BTM_VERSION.zip  
  
# Ensure signals are forwarded to the JVM process correctly for graceful
shutdown  
ENV LAUNCH_JBOSS_IN_BACKGROUND true  
  
# Expose the ports we're interested in  
EXPOSE 8080  
# Set the default command to run on boot  
# This will boot Hawkular and bind to all interface  
CMD ["/opt/jboss/hawkular-
btm/bin/standalone.sh","-b","0.0.0.0","-bmanagement","0.0.0.0"]  

