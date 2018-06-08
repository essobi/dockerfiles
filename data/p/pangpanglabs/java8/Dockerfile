FROM ubuntu:14.04  
MAINTAINER pangpanglab <pangpanglab@p2shop.cn>  
  
RUN apt-get update && apt-get install -y \  
apt-utils \  
net-tools \  
curl \  
vim \  
mysql-client libmysqlclient-dev \  
&& apt-get clean  
  
RUN mkdir -p /usr/java \  
&& curl -SL --header "Cookie: oraclelicense=accept-securebackup-cookie" \  
"http://download.oracle.com/otn-
pub/java/jdk/8u121-b13/e9e7ea248e2c4826b92b3f075a80e441/jdk-8u121-linux-x64.tar.gz"
\  
| tar -xzC /usr/java  
  
WORKDIR /usr/java  
RUN ln -s jdk1.8.0_121 latest  
  
ENV JAVA_HOME /usr/java/latest  
ENV PATH $JAVA_HOME/bin:$PATH  

