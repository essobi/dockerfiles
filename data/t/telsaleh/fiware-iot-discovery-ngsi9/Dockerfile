FROM ubuntu:14.04  
MAINTAINER Tarek Elsaleh <t.elsaleh@surrey.ac.uk>  
  
ENV BINARY_FILE http://iot.ee.surrey.ac.uk/fiware/releases/IOT-IoTDiscovery-
latest.zip  
  
RUN apt-get update && apt-get -y upgrade  
RUN apt-get --yes install software-properties-common debconf  
#RUN apt-get --yes install debconf  
RUN add-apt-repository ppa:webupd8team/java  
RUN apt-get --yes update  
  
# Accept the oracle license  
RUN echo "oracle-java8-installer shared/accepted-oracle-license-v1-1 boolean
true" | debconf-set-selections  
RUN apt-get --yes install oracle-java8-installer  
  
# tomcat7 installation  
RUN apt-get --yes install tomcat7 tomcat7-admin unzip  
RUN echo "JAVA_HOME=/usr/lib/jvm/java-8-oracle" >> /etc/default/tomcat7  
  
# Expose the default mysql port  
EXPOSE 3306  
#go to /tmp directory  
WORKDIR /tmp  
  
#get binary files  
RUN wget -q -O IOT-IoTDiscovery-latest.zip "$BINARY_FILE"  
RUN mkdir -p iotDiscovery  
RUN unzip IOT-IoTDiscovery-latest.zip -d iotDiscovery/  
WORKDIR /tmp/iotDiscovery  
RUN cp -r tomcat/s2w.war /var/lib/tomcat7/webapps  
RUN cp -r tomcat/ngsi9.war /var/lib/tomcat7/webapps  
RUN cp -r tomcat/tomcat-users.xml /var/lib/tomcat7/conf  
#RUN chmod 777 /var/run/mysqld/mysqld.sock && \  
# mysql installation  
RUN apt-get --yes install mysql-server mysql-client && \  
sleep 5 && \  
service mysql start && \  
mysql -u root < /tmp/iotDiscovery/sql/triple-store.sql  
  
# Expose the default tomcat port  
EXPOSE 8080  
# Start mysql and tomcat (and leave it hanging)  
CMD service mysql start && service tomcat7 start && tail -f
/var/lib/tomcat7/logs/catalina.out  

