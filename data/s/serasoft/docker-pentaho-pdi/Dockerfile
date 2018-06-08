#  
# Serasoft's docker image for Pentaho Data Integration  
#  
# VERSION 1.2  
#  
FROM serasoft/docker-jdk:jdk8  
MAINTAINER Sergio Ramazzina, sergio.ramazzina@serasoft.it  
  
# Set correct environment variables.  
ENV HOME /root  
ENV PENTAHO_HOME /opt/pentaho  
ENV PDI_HOME ${PENTAHO_HOME}/data-integration  
ENV BASE_REL 6.1  
ENV REV 0.1-196  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
# =============================== Start Image Customization
===================  
# Make sure base image is updated then install needed linux tools  
RUN apt-get update && \  
apt-get upgrade -f -y && \  
apt-get install -f -y wget curl git zip pwgen  
  
RUN useradd -m -d ${PENTAHO_HOME} pentaho  
  
# ADD pdi-ce-${BASE_REL}.${REV}.zip ${PENTAHO_HOME}/pdi-ce.zip  
RUN su -c "curl -L
http://sourceforge.net/projects/pentaho/files/Data%20Integration/${BASE_REL}/pdi-
ce-${BASE_REL}.${REV}.zip/download -o /opt/pentaho/pdi-ce.zip" pentaho && \  
su -c "unzip -q /opt/pentaho/pdi-ce.zip -d /opt/pentaho/" pentaho && \  
rm /opt/pentaho/pdi-ce.zip  
  
# Add all files needed t properly initialize the container  
COPY utils ${PDI_HOME}/utils  
COPY templates ${PDI_HOME}/templates  
  
# Set password to generated value  
RUN chown -Rf pentaho:pentaho ${PDI_HOME}  
  
ADD 01_init_container.sh /etc/my_init.d/01_init_container.sh  
  
ADD run /etc/service/pentaho/run  
  
RUN chmod +x /etc/my_init.d/*.sh && \  
chmod +x /etc/service/pentaho/run  
  
EXPOSE 8080  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

