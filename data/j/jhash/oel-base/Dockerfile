# Docker file to generate base Oracle Enterprise Linux Image  
FROM oraclelinux:7.0  
MAINTAINER jhash <sh3khar.jha@gmail.com>  
  
#### Basic package ####  
# Intial Size: 249M  
# Updated Size: ~713M  
# Final Size : 427M  
RUN yum -y update && \  
yum install -y wget tar unzip && \  
yum clean all  
ADD https://github.com/stedolan/jq/releases/download/jq-1.5/jq-linux64
/usr/bin/jq  
RUN chmod +x /usr/bin/jq  
  
#### JAVA ####  
## Open JDK  
# RUN yum install -y java-1.8.0-openjdk-headless && \  
# yum clean all  
## Oracle JDK  
ENV JDK_URL=http://download.oracle.com/otn-
pub/java/jdk/8u60-b27/jdk-8u60-linux-x64.tar.gz
JDK_FILE_PREFIX=jdk-8u60-linux-x64 JDK_FOLDER=jdk1.8.0_60  
  
RUN wget --no-cookies --no-check-certificate --header "Cookie:
gpw_e24=http%3A%2F%2Fwww.oracle.com%2F; oraclelicense=accept-securebackup-
cookie" "$JDK_URL" && \  
gunzip $JDK_FILE_PREFIX.tar.gz && \  
tar -xf $JDK_FILE_PREFIX.tar && \  
mv $JDK_FOLDER /opt/ && \  
ln -sf /opt/$JDK_FOLDER /opt/java && \  
rm $JDK_FILE_PREFIX.tar  
  
ENV JAVA_HOME=/opt/java  
  
#### Application Setup - OS ####  
ENV APP_NAME=app  
RUN groupadd $APP_NAME && \  
useradd --gid $APP_NAME \--home-dir /home/$APP_NAME \--create-home --shell
/bin/bash $APP_NAME && \  
mkdir /opt/$APP_NAME && \  
chown -R $APP_NAME:$APP_NAME /opt/$APP_NAME && \  
mkdir /var/$APP_NAME && \  
chown -R $APP_NAME:$APP_NAME /var/$APP_NAME  
  
#### s6 Overlay ####  
RUN cd /tmp/ && \  
wget --no-cookies --no-check-certificate https://github.com/just-
containers/s6-overlay/releases/download/v1.11.0.1/s6-overlay-amd64.tar.gz && \  
gunzip -c /tmp/s6-overlay-amd64.tar.gz | tar -xf - -C / && \  
rm /tmp/s6-overlay-amd64.tar.gz && \  
mv /etc/services.d /opt/$APP_NAME && \  
ln -sf /opt/$APP_NAME/services.d /etc/services.d && \  
chown -R $APP_NAME:$APP_NAME /opt/$APP_NAME/services.d  
  
VOLUME ["/var/$APP_NAME", "/opt/$APP_NAME"]  

