FROM ubuntu:14.04  
MAINTAINER Cornel  
  
# install Java 7 & curl  
RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" >
/etc/apt/sources.list.d/webupd8team-java.list && \  
echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" >>
/etc/apt/sources.list.d/webupd8team-java.list && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886 && \  
apt-get -y update && \  
/bin/echo debconf shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections && \  
DEBIAN_FRONTEND=noninteractive apt-get -y install oracle-java7-installer
oracle-java7-set-default tomcat7 curl  
  
# download and install spark  
RUN curl -s http://d3kbcqa49mib13.cloudfront.net/spark-1.3.0-bin-hadoop2.4.tgz
| tar -xz -C /usr/local/ && \  
mv /usr/local/spark-1.3.0-bin-hadoop2.4 /usr/local/spark  
  
# copy tomcat configuration file  
COPY tomcat7/context.xml /var/lib/tomcat7/conf/context.xml  
  
# copy some scripts to run Tomcat  
COPY scripts/start-tomcat.sh /start-tomcat.sh  
  
# copy spark dependencies for the job submission  
#COPY spark-job/* /home/  
#COPY job-dependencies/* /job-dependencies/  
# copy the Legis webapp  
COPY webapp/webapp-legis.war /var/lib/tomcat7/webapps/webapp-legis.war  
  
# configure spark  
#ENV SPARK_HOME /usr/local/spark  
# configure tomcat connections to Spark and Cassandra  
#ENV NETWORK_INTERFACE="eth0"  
ENV SPARK_MASTER="spark-master"  
ENV CASSANDRA="cassandra-001"  
ENV LOAD_BALANCER="load-balancer"  
### Tomcat ports  
# 8080: default website  
EXPOSE 8080  
# by default, this container is a Spark Worker  
CMD ["/start-tomcat.sh"]  

