# Leadware  
#  
# Oracle Java 8 Dockerfile  
# https://bitbucket.org/leadware/dockerfile-oracle-java8  
# https://jetune@bitbucket.org/leadware/dockerfile-oracle-java8.git  
# git@bitbucket.org:leadware/dockerfile-oracle-java8.git  
#  
# Pull base image.  
FROM ubuntu:16.04  
# Maintainer  
MAINTAINER Jean-Jacques ETUNÈ NGI<jetune@leadware.net>  
  
# Install Java.  
RUN \  
  
# Set default installation response [for non-interactive installation]  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
  
# Update APT  
apt-get update && \  
  
# Install Software properties commons  
apt-get install -y software-properties-common && \  
  
# Add Oracle JDK Repository  
add-apt-repository -y ppa:webupd8team/java && \  
  
# Update APT  
apt-get update && \  
  
# Install Oracle Java 8  
apt-get install -y oracle-java8-installer && \  
  
# Clear APT List  
rm -rf /var/lib/apt/lists/* && \  
# Remove Oracle Installer from de cache  
rm -rf /var/cache/oracle-jdk8-installer  
  
# Define working directory.  
WORKDIR /data  
  
# Define JAVA_HOME variable  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
# Define default command.  
CMD ["bash"]

