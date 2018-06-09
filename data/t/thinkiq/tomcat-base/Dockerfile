FROM ubuntu:16.04  
MAINTAINER Bruce McCleave<bruce@thinkiq.com>  
  
USER root  
ENV TOMCAT_VERSION=8.5.16 \  
JAVA_HOME=/usr/lib/jvm/java-8-oracle  
  
RUN apt-get update && \  
apt-get -y install software-properties-common && \  
apt-get update && \  
apt-get -y install sudo wget make gcc openssl curl && \  
apt-get install -y nodejs npm nodejs-legacy maven sudo nano vim git && \  
groupadd -r tomcat && useradd -r -g tomcat tomcat && \  
add-apt-repository ppa:webupd8team/java && \  
apt-get update && \  
echo debconf shared/accepted-oracle-license-v1-1 select true | sudo debconf-
set-selections && \  
echo debconf shared/accepted-oracle-license-v1-1 seen true | sudo debconf-set-
selections && \  
apt-get install -y oracle-java8-installer && \  
cd /usr/lib/jvm/ && \  
cd /tmp && \  
wget http://www-
eu.apache.org/dist/tomcat/tomcat-8/v$TOMCAT_VERSION/bin/apache-
tomcat-$TOMCAT_VERSION.tar.gz && \  
tar xvzf apache-tomcat-$TOMCAT_VERSION.tar.gz && \  
mv apache-tomcat-$TOMCAT_VERSION /opt/tomcat2 && \  
rm apache-tomcat-$TOMCAT_VERSION.tar.gz && \  
cd /opt/tomcat2 && \  
chown -R tomcat:tomcat /opt/tomcat2 && \  
rm -r webapps/ROOT/ && \  
apt-get -y install libapr1 libapr1-dev libtcnative-1 && \  
cd /tmp && \  
wget http://www-us.apache.org/dist/apr/apr-1.6.2.tar.gz && \  
tar zxvf apr-1.6.2.tar.gz && \  
cd apr-1.6.2 && \  
./configure && \  
make && \  
make install && \  
wget http://www-us.apache.org/dist/tomcat/tomcat-
connectors/native/1.2.12/source/tomcat-native-1.2.12-src.tar.gz && \  
tar -xzf tomcat-native-1.2.12-src.tar.gz && \  
cd tomcat-native-1.2.12-src/native && \  
./configure --with-apr=/usr/local/apr \--with-java-home=$JAVA_HOME && \  
make && \  
make install && \  
npm install -g npm@4 && \  
npm install -g bower-installer && \  
npm install -g gulp && \  
cd /tmp && \  
curl -L -O
https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-5.4.3-amd64.deb
&& \  
dpkg -i filebeat-5.4.3-amd64.deb && \  
apt-get upgrade -y && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

