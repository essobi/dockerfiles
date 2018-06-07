# docker-tomcat  
#  
# VERSION 1.0  
FROM ubuntu:14.04.2  
MAINTAINER EricoGR <ericomercial@yahoo.com.br>  
  
#instala o mínimo para instalação dos pacotes  
RUN \  
apt-get update && \  
apt-get install -y software-properties-common  
  
#instalação do jdk  
RUN \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y oracle-java8-installer && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/oracle-jdk8-installer  
  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
ENV TOMCAT_VERSION 8.0.24  
ENV TOMCAT_DIR /opt/apache-tomcat  
ENV TOMCAT_NAME apache-tomcat-$TOMCAT_VERSION  
ENV TOMCAT_FILENAME $TOMCAT_NAME.tar.gz  
  
#instala o tomcat  
RUN \  
wget
http://ftp.unicamp.br/pub/apache/tomcat/tomcat-8/v$TOMCAT_VERSION/bin/$TOMCAT_FILENAME
&& \  
tar zxvf $TOMCAT_FILENAME && \  
mv $TOMCAT_NAME /opt && \  
ln -s /opt/$TOMCAT_NAME $TOMCAT_DIR && \  
rm $TOMCAT_FILENAME  
  
ADD ["tomcat-users.xml", "$TOMCAT_DIR/conf/tomcat-users.xml"]  
  
EXPOSE 8080  
CMD $TOMCAT_DIR/bin/catalina.sh run  

