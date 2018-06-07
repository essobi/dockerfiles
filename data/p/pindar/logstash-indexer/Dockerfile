FROM ubuntu:14.04  
MAINTAINER Simon Dittlmann <simon.dittlmann@tado.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
ENV JAVA_VERSION 8u31  
ENV JAVA_FOLDER_NAME jdk1.8.0_31  
RUN apt-get update -qq && \  
apt-get install -y wget gzip curl && \  
cd /tmp && wget --no-cookies --header "Cookie:
gpw_e24=http%3A%2F%2Fwww.oracle.com; oraclelicense=accept-securebackup-cookie;
s_nr=1394181036342;" http://download.oracle.com/otn-
pub/java/jdk/${JAVA_VERSION}-b13/jdk-${JAVA_VERSION}-linux-x64.tar.gz && \  
gzip -d jdk-${JAVA_VERSION}-linux-x64.tar.gz && \  
tar -xf jdk-${JAVA_VERSION}-linux-x64.tar && \  
mkdir -p /opt/Oracle_Java && \  
mv /tmp/${JAVA_FOLDER_NAME} /opt/Oracle_Java/${JAVA_FOLDER_NAME} && \  
sudo update-alternatives --install "/usr/bin/java" "java"
"/opt/Oracle_Java/${JAVA_FOLDER_NAME}/bin/java" 1 && \  
sudo update-alternatives --install "/usr/bin/javac" "javac"
"/opt/Oracle_Java/${JAVA_FOLDER_NAME}/bin/javac" 1 && \  
sudo update-alternatives --install "/usr/bin/javaws" "javaws"
"/opt/Oracle_Java/${JAVA_FOLDER_NAME}/bin/javaws" 1 && \  
sudo update-alternatives --install "/usr/bin/jar" "jar"
"/opt/Oracle_Java/${JAVA_FOLDER_NAME}/bin/jar" 1 && \  
sudo update-alternatives --set "java"
"/opt/Oracle_Java/${JAVA_FOLDER_NAME}/bin/java" && \  
sudo update-alternatives --set "javac"
"/opt/Oracle_Java/${JAVA_FOLDER_NAME}/bin/javac" && \  
sudo update-alternatives --set "javaws"
"/opt/Oracle_Java/${JAVA_FOLDER_NAME}/bin/javaws" && \  
sudo update-alternatives --set "jar"
"/opt/Oracle_Java/${JAVA_FOLDER_NAME}/bin/jar" && \  
rm -rf /tmp/jdk-${JAVA_VERSION}-linux-x64.tar  
  
# Install logstash shipper  
ENV LOGSTASH_VERSION 1.4.2  
ENV LOGSTASH_HOME /logstash/logstash-${LOGSTASH_VERSION}  
RUN curl -L -o /tmp/logstash.tar.gz
https://download.elasticsearch.org/logstash/logstash/logstash-${LOGSTASH_VERSION}.tar.gz
&& \  
mkdir -p /logstash && \  
tar zxvf /tmp/logstash.tar.gz -C /logstash && \  
rm -rf /tmp/logstash.tar.gz  
  
COPY indexer.conf $LOGSTASH_HOME/conf/indexer.conf  
  
COPY start.sh /start.sh  
RUN chmod +x /start.sh  
  
CMD ["/start.sh"]  

