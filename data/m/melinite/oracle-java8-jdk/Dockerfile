# use with docker 1.4.1+ recommended  
# webupd8 oracle java 8 from very lightweight google/debian:wheezy  
  
FROM google/debian:wheezy  
MAINTAINER David Seong <melinite@gmail.com>  
  
# Always define userspace; security is going to be an ongoing issue with
popularity of Docker.  
# Beware of privilege escalation and do not trust arbitrary docker files
blindly.  
USER root  
ENV DEBIAN_FRONTEND=noninteractive JAVA_HOME=/usr/lib/jvm/java-8-oracle  
# Install Java  
RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" |
tee /etc/apt/sources.list.d/webupd8team-java.list && \  
echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" |
tee -a /etc/apt/sources.list.d/webupd8team-java.list && \  
echo "oracle-java8-installer shared/accepted-oracle-license-v1-1 select true"
| debconf-set-selections && \  
apt-key adv \--keyserver hkp://keyserver.ubuntu.com:80 \--recv-keys EEA14886
&& \  
apt-get update && \  
apt-get install -y \--force-yes \--no-install-recommends ca-certificates
oracle-java8-installer && \  
apt-get clean all && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
rm -rf /var/cache/oracle-jdk8-installer  

