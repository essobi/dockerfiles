#  
# Oracle Java 8 Dockerfile from  
#  
# https://github.com/dockerfile/java  
# https://github.com/dockerfile/java/tree/master/oracle-java8  
#  
# Using https://github.com/phusion/baseimage-docker as a base image  
FROM phusion/baseimage:latest  
MAINTAINER Diego Schmidt <dceschmidt@gmail.com>  
ENV DEBIAN_FRONTEND noninteractive  
  
# Set correct environment variables.  
ENV HOME /root  
  
# Use baseimage-docker's init system  
CMD ["/sbin/my_init"]  
  
# Install Java.  
RUN \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y oracle-java8-installer && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/oracle-jdk8-installer  
  
# Define commonly used JAVA_HOME variable  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
  
# Download keybox  
ADD https://github.com/skavanagh/KeyBox/releases/download/v2.60.00/keybox-
jetty-v2.60_00.tar.gz /opt/  
RUN tar -zxf /opt/keybox-jetty-v2.60_00.tar.gz -C /opt  
RUN mv /opt/KeyBox-jetty /opt/keybox  
RUN rm /opt/keybox-jetty-v2.60_00.tar.gz  
  
# Expose the http port  
expose 8443  
# Clean up APT when done.  
# RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
# Add edge.sh to execute during container startup  
RUN mkdir -p /etc/my_init.d  
ADD edge.sh /etc/my_init.d/edge.sh  
RUN chmod +x /etc/my_init.d/edge.sh  
  
# Add Keybox to runit  
RUN mkdir /etc/service/keybox  
ADD keybox.sh /etc/service/keybox/run  
RUN chmod +x /etc/service/keybox/run

