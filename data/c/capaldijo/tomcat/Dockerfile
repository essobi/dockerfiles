#  
# Oracle Java 8 & Maven Dockerfile  
#  
# Pull base image.  
FROM debian:jessie  
  
MAINTAINER capaldijo  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV TOMCAT_HOME=/opt/apache-tomcat-8.0.43  
RUN echo /usr/bin/debconf shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections  
  
RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" |
tee /etc/apt/sources.list.d/webupd8team-java.list && \  
echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" |
tee -a /etc/apt/sources.list.d/webupd8team-java.list && \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886 &&
\  
apt-get -y update && \  
apt-get install -yq oracle-java8-installer oracle-java8-set-default && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/oracle-jdk8-installer && \  
rm -rf /var/lib/apt/lists/*  
  
WORKDIR /tmp  
  
RUN wget http://wwwftp.ciril.fr/pub/apache/tomcat/tomcat-8/v8.0.43/bin/apache-
tomcat-8.0.43.tar.gz && \  
tar xzvf apache-tomcat-8.0.43.tar.gz -C /opt/ && \  
rm -rf apache-tomcat-$TOMCAT_VERSION.tar.gz && \  
rm -rf /tmp  
  
WORKDIR /  
  
ADD files/tomcat-run.sh /tomcat-run.sh  
ADD files/settings.xml $TOMCAT_HOME/conf/settings.xml  
ADD files/tomcat-users.xml $TOMCAT_HOME/conf/tomcat-users.xml  
RUN chmod 755 /*.sh  
  
EXPOSE 8080 8009  
ENTRYPOINT ["/tomcat-run.sh"]  

