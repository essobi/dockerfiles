#  
# MongoDB Dockerfile  
#  
# https://github.com/dockerfile/mongodb  
#  
# Pull base image.  
FROM ubuntu:16.04  
RUN apt-get update  
RUN apt-get dist-upgrade -y  
RUN apt-get install -y software-properties-common python-software-properties  
  
# Install MongoDB.  
RUN \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10 && \  
echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen'
> /etc/apt/sources.list.d/mongodb.list && \  
apt-get update && \  
apt-get install -y mongodb-org && \  
rm -rf /var/lib/apt/lists/*  
  
# Define mountable directories.  
VOLUME ["/data/db"]  
  
# Expose ports.  
# - 27017: process  
# - 28017: http  
EXPOSE 27017  
EXPOSE 28017  
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
EXPOSE 8080  
# Install Python.  
RUN \  
apt-get update && \  
apt-get install -y python python-dev python-pip python-virtualenv && \  
rm -rf /var/lib/apt/lists/*  
  
# Install Node  
# curl -sL https://deb.nodesource.com/setup_9.x | sudo -E bash - && \  
#RUN \  
# apt-get -qq update && \  
# apt-get install -y nodejs && \  
# apt-get install -y npm  
RUN apt-get update  
RUN apt-get install --yes curl  
RUN curl --silent --location https://deb.nodesource.com/setup_8.x | bash -  
RUN apt-get install --yes nodejs  
RUN apt-get install --yes build-essential  
  
RUN npm install local-web-server -g  
EXPOSE 8079  
# Define working directory.  
RUN addgroup mygroup && useradd -G mygroup myuser && mkdir -p /usr/src/app &&
chown -R myuser /usr/src/app  
  
# Define default command.  
WORKDIR /usr/src/app  
VOLUME ["/usr/src/app"]  
COPY entry.sh /usr/src/app/  
COPY portal /usr/src/app/  
COPY service /usr/src/app/  
RUN ["chmod", "777", "/usr/src/app/entry.sh"]  
RUN ["chown", "-R","myuser","/usr/src/app"]  
USER myuser  
ENTRYPOINT ["/usr/src/app/entry.sh"]  

