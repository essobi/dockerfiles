#  
# author: sheng (mailto:shanshengsheng@gmail.com)  
#  
FROM centos:7  
LABEL maintainer="shanshengsheng@gmail.com" \  
provider="SSS, Ltd."  
  
ENV LANG="en_US.UTF-8" \  
LANGUAGE="en_US:en" \  
LC_ALL="en_US.UTF-8"  
ENV JAVA_VERSION="1.8.0_172"  
ENV JAVA_HOME="/usr/local/jdk${JAVA_VERSION}"  
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
pub/java/jdk/8u172-b11/a58eab1ec242421181065cdc37240b08/jdk-8u172-linux-x64.tar.gz
\  
-O /tmp/jdk.tar.gz \  
&& tar -zxf /tmp/jdk.tar.gz -C /usr/local/ \  
&& \rm -f /tmp/jdk.tar.gz ${JAVA_HOME}/src.zip ${JAVA_HOME}/javafx-src.zip  
  
# Find avaliable downloads  
# curl -s
http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html
| \  
# awk "/downloads\\['/ && ! /demos/ && /\\['files'\\]\\['jdk/"  

