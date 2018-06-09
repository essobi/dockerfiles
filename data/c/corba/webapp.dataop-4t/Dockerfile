FROM ubuntu:16.04  
MAINTAINER Cornel  
  
  
# set environmental variables used to generate this image  
ENV DEBIAN_FRONTEND noninteractive  
ENV TOMCAT tomcat8  
ENV JAVA java8  
  
# install Java, Tomcat and supervisor  
RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" >
/etc/apt/sources.list.d/webupd8team-java.list \  
&& echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main"
>> /etc/apt/sources.list.d/webupd8team-java.list \  
&& apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886 \  
&& apt-get -y update \  
&& /bin/echo debconf shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections \  
&& apt-get -y install oracle-${JAVA}-installer oracle-${JAVA}-set-default \  
&& apt-get -y install ${TOMCAT} \  
&& apt-get -y install supervisor  
  
# copy tomcat configuration file  
COPY tomcat-conf/server.xml /var/lib/${TOMCAT}/conf/  
  
# copy some scripts to run Tomcat  
COPY scripts/start-tomcat.sh /usr/bin/start-tomcat.sh  
  
# copy the Database Operations webapp  
COPY webapps/dataop.war /var/lib/${TOMCAT}/webapps/  
  
# Supervisor config  
COPY supervisor/tomcat.conf /etc/supervisor/conf.d/  
  
# copy Database Operations dependencies  
COPY webapps-dep/mysql-connector-java-5.1.10-bin.jar /usr/share/${TOMCAT}/lib/  
  
### set the environmental variables used inside this container  
ENV MYSQL="mysql"  
ENV LOAD_BALANCER_SERVICE="load-balancer.service.dataop"  
ENV LOAD_BALANCER_ANALYTICS="load-balancer.analytics.dataop"  
### Tomcat ports  
# 9200: Auto-switching mechanism to select either a blocking Java based
connector or an APR/native based connector  
# 9201: Blocking Java connector  
# 9202: Non-blocking Java connector  
# 9203: The APR/native connector  
EXPOSE 9200 9201 9202 9203  
# The main process of this container is supervisor  
CMD ["supervisord", "-n"]  
  

