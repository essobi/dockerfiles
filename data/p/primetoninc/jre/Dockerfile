#  
# Copyright (c) 2001-2018 Primeton Technologies, Ltd.  
# All rights reserved.  
#  
# author: ZhongWen Li (mailto:lizw@primeton.com)  
#  
FROM centos:7  
LABEL maintainer="lizw@primeton.com" \  
provider="Primeton Technologies, Ltd."  
  
ENV LANG="en_US.UTF-8" \  
LANGUAGE="en_US:en" \  
LC_ALL="en_US.UTF-8"  
ENV JAVA_VERSION="1.8.0_152"  
ENV JAVA_HOME="/usr/local/jdk${JAVA_VERSION}"  
ENV JRE_HOME=${JAVA_HOME}  
  
ENV PATH="${PATH}:${JAVA_HOME}/bin"  
# Do not use alias cp  
RUN \cp -f /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \  
&& yum update -y \  
&& yum install -y zip unzip tar curl wget \  
&& echo "alias l='ls -al'" >> /root/.bashrc  
  
# ADD resources/jdk*.tar.gz /usr/local/  
RUN wget --tries=3 \  
\--header "Cookie: oraclelicense=accept-securebackup-cookie" \  
http://download.oracle.com/otn-
pub/java/jdk/8u152-b16/aa0333dd3019491ca4f6ddbe78cdb6d0/server-
jre-8u152-linux-x64.tar.gz \  
-O /tmp/jre.tar.gz \  
&& tar -zxf /tmp/jre.tar.gz -C /usr/local/ \  
&& \rm -f /tmp/jre.tar.gz ${JAVA_HOME}/src.zip ${JAVA_HOME}/javafx-src.zip  

