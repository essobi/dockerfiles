FROM ubuntu:16.04  
MAINTAINER Cornel  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV TOMCAT tomcat7  
  
# install Java, Tomcat, supervisor  
RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" >
/etc/apt/sources.list.d/webupd8team-java.list \  
&& echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main"
>> /etc/apt/sources.list.d/webupd8team-java.list \  
&& apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886 \  
&& apt-get -y update \  
&& echo debconf shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections \  
&& apt-get -y install oracle-java8-installer oracle-java8-set-default \  
&& apt-get -y install ${TOMCAT} \  
&& apt-get -y install supervisor \  
&& rm -rf /var/lib/apt/lists/* \  
&& apt-get clean  
  
# copy the script that starts Tomcat  
COPY scripts/start-tomcat.sh /usr/bin/start-tomcat.sh  
  
# Supervisor config  
COPY supervisor/tomcat.conf /etc/supervisor/conf.d/  
  
# copy the π webapp  
COPY webapp/wordcount.war /var/lib/${TOMCAT}/webapp/wordcount.war  
  
### Tomcat ports  
# 8080: default website  
EXPOSE 8080  
# The main process of this container is supervisor  
CMD ["supervisord", "-n"]

