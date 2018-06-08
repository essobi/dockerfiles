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
ENV JAVA_VERSION="1.7.0_80"  
ENV JAVA_HOME="/usr/local/jdk${JAVA_VERSION}"  
ENV PATH="${PATH}:${JAVA_HOME}/bin"  
# Do not use alias cp  
RUN \cp -f /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \  
&& yum update -y \  
&& yum install -y zip unzip tar curl \  
&& echo "alias l='ls -al'" >> /root/.bashrc  
  
# ADD resources/jdk*.tar.gz /usr/local/  
RUN curl --fail --location --retry 3 \  
\--header "Cookie: oraclelicense=accept-securebackup-cookie" \  
http://ftp.osuosl.org/pub/funtoo/distfiles/oracle-
java/jdk-7u80-linux-x64.tar.gz \  
-o /tmp/jdk.tar.gz \  
&& tar -zxf /tmp/jdk.tar.gz -C /usr/local/ \  
&& \rm -f /tmp/jdk.tar.gz ${JAVA_HOME}/src.zip ${JAVA_HOME}/javafx-src.zip  

