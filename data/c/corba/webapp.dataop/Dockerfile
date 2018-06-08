FROM ubuntu:16.04  
MAINTAINER Cornel  
  
# install Java 7 & curl  
RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" >
/etc/apt/sources.list.d/webupd8team-java.list \  
&& echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main"
>> /etc/apt/sources.list.d/webupd8team-java.list \  
&& apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886 \  
&& apt-get -y update \  
&& /bin/echo debconf shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections \  
&& DEBIAN_FRONTEND=noninteractive apt-get -y install oracle-java8-installer
oracle-java8-set-default tomcat8 curl  
  
  
# copy tomcat configuration file  
COPY tomcat-conf/server.xml /var/lib/tomcat8/conf/  
# copy some scripts to run Tomcat  
COPY scripts/start-tomcat.sh /start-tomcat.sh  
  
# copy the Database Operations webapp  
COPY webapp/dataop.war /var/lib/tomcat8/webapps/  
# copy Database Operations dependencies  
COPY webapp-dep/mysql-connector-java-5.1.10-bin.jar /usr/share/tomcat8/lib/  
# configure tomcat connections to Spark and Cassandra  
#ENV NETWORK_INTERFACE="eth0"  
ENV MYSQL="mysql"  
ENV LOAD_BALANCER="load-balancer"  
### Tomcat ports  
# 9200: Auto-switching mechanism to select either a blocking Java based
connector or an APR/native based connector  
# 9201: Blocking Java connector  
# 9202: Non-blocking Java connector  
# 9203: The APR/native connector  
  
  
EXPOSE 9200 9201 9202 9203  
# by default, this container is a Spark Worker  
CMD ["/start-tomcat.sh"]  

