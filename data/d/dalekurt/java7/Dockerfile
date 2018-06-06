# Oracle Java 7 for Ubuntu 14.04  
#  
# GitHub - http://github.com/dalekurt/docker-java7  
# Docker Hub - http://hub.docker.com/u/dalekurt/docker-java7  
# Twitter - http://www.twitter.com/dalekurt  
# Latest Ubuntu LTS from stackbrew  
FROM stackbrew/ubuntu:14.04  
MAINTAINER Dale-Kurt Murray "dalekurt.murray@gmail.com"  
# Add Repository  
RUN \  
echo "===> add webupd8 repository..." && \  
echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" | tee
/etc/apt/sources.list.d/webupd8team-java.list && \  
echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" |
tee -a /etc/apt/sources.list.d/webupd8team-java.list && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886 && \  
apt-get update && \  
\  
\  
echo "===> install Java" && \  
echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-
selections && \  
echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-
selections && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y --force-yes oracle-
java7-installer oracle-java7-set-default && \  
\  
\  
echo "===> clean up..." && \  
rm -rf /var/cache/oracle-jdk7-installer && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
  
# define default command  
CMD ["java"]  

