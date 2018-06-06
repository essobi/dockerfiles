FROM clifton/debian-base  
MAINTAINER Clifton King <cliftonk@gmail.com>  
  
ENV JAVA_VERSION 1.8.0  
  
RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" \  
| tee /etc/apt/sources.list.d/webupd8team-java.list \  
&& echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main"
\  
| tee -a /etc/apt/sources.list.d/webupd8team-java.list \  
&& apt-key adv --keyserver keyserver.ubuntu.com \--recv-keys EEA14886 \  
&& echo "oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true" \  
| /usr/bin/debconf-set-selections \  
&& apt-get update \  
&& apt-get install -y \  
python-software-properties=0.82.7.1debian1 \  
oracle-java8-installer=8u31+8u33arm-1~webupd8~1 \  
&& update-alternatives --display java \  
&& rm -rf /var/lib/apt/lists/* \  
&& apt-get clean  
  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  

