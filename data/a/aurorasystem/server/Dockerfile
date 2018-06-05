FROM centos:7  
MAINTAINER Aurora System <it@aurora-system.com>  
  
  
# Dependence  
RUN yum install -y wget gcc automake autoconf libtool make gcc-c++ gtk2
libXtst cmake bison libXaw && yum clean all  
  
# Oracle Java 1.8  
RUN \  
cd /tmp && \  
wget --header "Cookie: oraclelicense=accept-securebackup-cookie"
http://download.oracle.com/otn-pub/java/jdk/8u102-b14/jdk-8u102-linux-x64.rpm
&& \  
yum localinstall -y jdk-8u102-linux-x64.rpm && yum clean all && \  
echo 'export JAVA_HOME=/usr/java/jdk1.8.0_102/' >> /etc/profile && \  
echo 'export JRE_HOME=/usr/java/jdk1.8.0_102/jre' >> /etc/profile && \  
echo 'export PATH=$PATH:$HOME/bin:$JAVA_HOME/bin' >> /etc/profile && \  
source /etc/profile && \  
rm -r /tmp/*  
  
# Zeromq  
RUN \  
cd /tmp && \  
wget
https://github.com/zeromq/zeromq3-x/releases/download/v3.2.5/zeromq-3.2.5.tar.gz
&& \  
tar -zxf zeromq-3.2.5.tar.gz && cd zeromq-3.2.5/ && \  
./configure && make && make install && \  
rm -r /tmp/*  
  
# jzmq  
RUN \  
cd /tmp && \  
wget https://github.com/zeromq/jzmq/archive/v3.1.0.tar.gz && \  
tar -zxf v3.1.0.tar.gz && cd jzmq-3.1.0/ && \  
./autogen.sh && ./configure && make && make install && \  
rm -r /tmp/*  
  
# Translayout need  
RUN mkdir -p /usr/share/fonts/wqy-microhei  
ADD ./wqy-microhei.ttc /usr/share/fonts/wqy-microhei/wqy-microhei.ttc  
RUN fc-cache /usr/share/fonts/wqy-microhei  
#RUN useradd -ms /bin/bash deploy  
#USER deploy  
RUN mkdir -p /app  
WORKDIR /app  

