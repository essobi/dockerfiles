FROM ubuntu:16.04  
MAINTAINER Bruce McCleave<bruce@thinkiq.com>  
  
USER root  
ENV TOMCAT_VERSION=8.5.11 JAVA_HOME=/usr/lib/jvm/default-java  
RUN apt-get update && \  
apt-get -y install software-properties-common && \  
apt-get update && \  
apt-get -y install sudo wget make gcc openssl && \  
useradd tomcat && \  
add-apt-repository ppa:webupd8team/java && \  
apt-get update && \  
echo debconf shared/accepted-oracle-license-v1-1 select true | sudo debconf-
set-selections && \  
echo debconf shared/accepted-oracle-license-v1-1 seen true | sudo debconf-set-
selections && \  
apt-get install -y oracle-java8-installer && \  
cd /usr/lib/jvm/ && \  
ln -s java-8-oracle default-java && \  
cd /tmp && \  
wget http://www-
eu.apache.org/dist/tomcat/tomcat-8/v$TOMCAT_VERSION/bin/apache-
tomcat-$TOMCAT_VERSION.tar.gz && \  
tar xvzf apache-tomcat-$TOMCAT_VERSION.tar.gz && \  
mv apache-tomcat-$TOMCAT_VERSION /opt/tomcat2 && \  
rm apache-tomcat-$TOMCAT_VERSION.tar.gz && \  
cd /opt/tomcat2 && \  
chown -R tomcat conf && \  
chown -R tomcat logs && \  
chown -R tomcat temp && \  
chown -R tomcat webapps && \  
chown -R tomcat work && \  
rm -r webapps/ROOT/ && \  
apt-get -y install libapr1 libapr1-dev libtcnative-1 && \  
cd /tmp && \  
wget http://www-us.apache.org/dist/apr/apr-1.5.2.tar.gz && \  
tar zxvf apr-1.5.2.tar.gz && \  
cd apr-1.5.2 && \  
sudo ./configure && \  
sudo make && \  
sudo make install && \  
cd /tmp && \  
wget http://www-us.apache.org/dist/tomcat/tomcat-
connectors/native/1.2.10/source/tomcat-native-1.2.10-src.tar.gz && \  
tar -xzf tomcat-native-1.2.10-src.tar.gz && \  
cd tomcat-native-1.2.10-src/native && \  
./configure --with-apr=/usr/local/apr \--with-java-home=$JAVA_HOME && \  
make && \  
make install && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

