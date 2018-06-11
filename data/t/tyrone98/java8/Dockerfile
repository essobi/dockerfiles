FROM debian:jessie  
  
MAINTAINER Tyrone <tyrone.dev@gmail.com>  
  
# install oracle java 8  
RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" >
/etc/apt/sources.list.d/webupd8team-java.list \  
&& echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main"
>> /etc/apt/sources.list.d/webupd8team-java.list \  
&& apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886 \  
&& echo "oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true" | debconf-set-selections \  
&& apt-get update \  
&& apt-get -qy install oracle-java8-installer \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /var/cache/oracle-
jdk8-installer  
# set environment  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  

