FROM ubuntu:14.04  
MAINTAINER Suku  
  
RUN \  
apt-get -qq update && \  
DEBIAN_FRONTEND=noninteractive apt-get -qq -y install wget exuberant-ctags
unzip default-jre-headless && \  
wget -q -O /tmp/apache-tomcat.tar.gz \  
http://apache.mirror.amaze.com.au/tomcat/tomcat-8/v8.5.6/bin/apache-
tomcat-8.5.6.tar.gz && \  
wget -q -O /tmp/opengrok.tar.gz.zip \  
https://github.com/OpenGrok/OpenGrok/files/467358/opengrok-0.12.1.6.tar.gz.zip
&& \  
tar xf /tmp/apache-tomcat* -C /opt/ && \  
unzip /tmp/opengrok* -d /tmp && tar xf /tmp/opengrok*.tar.gz -C /opt/ && \  
ln -s /opt/apache-tomcat* /opt/tomcat && \  
ln -s /opt/opengrok* /opt/opengrok && \  
apt-get -qq -y remove \--purge unzip wget vim-tiny vim-common man && \  
apt-get -qq -y autoremove && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /tmp/* && \  
mkdir -p /var/opengrok/{data,src,etc} && \  
echo "JAVA_HOME=$(dirname $(dirname $(readlink -f $(which java))))" >>
/etc/environment  
  
ENV CATALINA_HOME /opt/tomcat  
ENV OPENGROK_TOMCAT_BASE ${CATALINA_HOME}  
  
RUN /opt/opengrok/bin/OpenGrok deploy  
  
CMD /opt/opengrok/bin/OpenGrok index; /opt/tomcat/bin/catalina.sh run  
  
EXPOSE 8080  

