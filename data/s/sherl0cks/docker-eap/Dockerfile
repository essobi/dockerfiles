FROM jboss/base-jdk:8  
#ADD http://download.eng.rdu2.redhat.com/released/JBEAP-6/6.4.4/jboss-
eap-6.4.4-full-build.zip /tmp/eap  
####### MAINTAINER ############  
MAINTAINER "Justin Holmes" "jholmes@redhat.com"  
####### ENVIRONMENT ############  
ENV ARTIFACT_REPOSITORY http://209.132.179.144  
ENV EAP_VERSION 6.4.6  
ENV JBOSS_HOME /opt/jboss/jboss-eap-6.4  
RUN cd /opt/jboss/ \  
&& curl -O $ARTIFACT_REPOSITORY/jboss-eap-$EAP_VERSION-full-build.zip \  
&& unzip -q jboss-eap-$EAP_VERSION-full-build.zip -d . \  
&& rm jboss-eap-$EAP_VERSION-full-build.zip  
  
# Expose the ports we're interested in  
EXPOSE 8080  
# Set the default command to run on boot  
# This will boot EAP in the standalone mode and bind to all interface  
CMD ["/opt/jboss/jboss-eap-6.4/bin/standalone.sh", "-b", "0.0.0.0"]  

