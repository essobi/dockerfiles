FROM ubuntu:14.04  
  
MAINTAINER Joe Bullard <jbullard@cogent.co.jp>  
  
RUN apt-get update \  
&& apt-get install -y software-properties-common \  
&& add-apt-repository ppa:webupd8team/java -y \  
&& apt-get update \  
&& echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true
\  
| /usr/bin/debconf-set-selections \  
&& apt-get install -y oracle-java8-installer \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /var/cache/oracle-jdk8-installer  
  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle/  

