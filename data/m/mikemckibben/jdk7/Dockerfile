FROM debian:latest  
MAINTAINER mikemckibben@gmail.com  
  
ENV JDK_VERSION 1.7.0_71  
ENV JAVA_HOME /usr/local/jdk${JDK_VERSION}  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get -y update && \  
apt-get -y upgrade && \  
apt-get -y install apt-utils && \  
apt-get -y install locales curl wget vim build-essential zip unzip \  
libc6 libstdc++6 libcups2 liblcms2-2 libjpeg8 libnss3 libfontconfig1 \  
libfreetype6 libglib2.0-0 libkrb5-3 libpcsclite1 zlib1g ttf-dejavu-extra  
RUN (echo "en_US ISO-8859-1" && echo "en_US.UTF-8 UTF-8") > /etc/locale.gen &&
locale-gen  
ENV LC_ALL en_US.UTF-8  
WORKDIR /usr/local  
RUN (wget -q -O - \  
\--no-check-certificate --no-cookies \  
\--header "Cookie: oraclelicense=accept-securebackup-cookie" \  
http://download.oracle.com/otn-pub/java/jdk/7u71-b14/jdk-7u71-linux-x64.tar.gz
| \  
tar --no-same-owner -xzf - ) && \  
(cd /tmp && \  
wget -q --no-check-certificate --no-cookies \  
\--header "Cookie: oraclelicense=accept-securebackup-cookie" \  
http://download.oracle.com/otn-pub/java/jce/7/UnlimitedJCEPolicyJDK7.zip && \  
unzip -oj -d ${JAVA_HOME}/jre/lib/security UnlimitedJCEPolicyJDK7.zip
\\*/\\*.jar && \  
rm UnlimitedJCEPolicyJDK7.zip)  
  
ENV PATH $JAVA_HOME/bin:$PATH  
WORKDIR /root  
CMD ["/bin/bash"]  

