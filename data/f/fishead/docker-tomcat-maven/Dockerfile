# version: 0.1  
  
FROM tomcat  
MAINTAINER Zhang Zh. <zhchuan7@gmail.com>  
  
ENV LANG C.UTF-8  
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64  
  
RUN echo 'deb http://deb.debian.org/debian jessie-backports main' >
/etc/apt/sources.list.d/jessie-backports.list \  
&& apt-get update \  
&& apt-get install -y \  
openjdk-8-jdk \  
ca-certificates-java=20161107~bpo8+1 \  
maven \  
&& rm -rf /var/lib/apt/lists/* \  
&& /var/lib/dpkg/info/ca-certificates-java.postinst configure  

