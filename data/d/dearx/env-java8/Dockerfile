############################################################  
# Dockerfile to build java 8 container images  
# Based on phusion/baseimage  
############################################################  
# Set the base image to phusion/baseimage  
FROM phusion/baseimage:latest  
CMD ["/sbin/my_init"]  
  
LABEL maintainer "Jonathan Temlett - Daedalus Solutions (jono@daedalus.co.za)"  
  
#ARG VCS_REF  
#LABEL org.label-schema.vcs-ref=$VCS_REF \  
# org.label-schema.vcs-url="https://bitbucket.org/temdu/env-java"  
  
RUN apt-get update && \  
apt-get install -y software-properties-common python-software-properties && \  
add-apt-repository ppa:webupd8team/java && \  
apt-get update && \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections && \  
apt-get install -y oracle-java8-installer && \  
apt-get install oracle-java8-set-default && \  
rm -rf /var/cache/oracle-jdk8-installer  
ENV JAVA_HOME="/usr/lib/jvm/java-8-oracle/"  
  
CMD ["java"]

