FROM debian:jessie  
MAINTAINER Committed Software <docker@committed.software>  
  
# Install Java 8: http://www.webupd8.org/2014/03/how-to-install-oracle-
java-8-in-debian.html  
# Note we also install some useful utilities  
RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" |
tee /etc/apt/sources.list.d/webupd8team-java.list \  
&& echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main"
| tee -a /etc/apt/sources.list.d/webupd8team-java.list \  
&& apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886
\  
&& apt-get update \  
&& echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true
| debconf-set-selections \  
&& apt-get install -y unzip curl ca-certificates wget \  
&& apt-get install -y oracle-java8-installer oracle-java8-set-default \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& rm -rf /var/cache/oracle-jdk8-installer \  
&& rm -rf /usr/lib/jvm/java-8-oracle/*src.zip
/usr/lib/jvm/java-8-oracle/lib/missioncontrol
/usr/lib/jvm/java-8-oracle/lib/visualvm \  
&& mkdir /java  
  
WORKDIR /java  
VOLUME /java  
ENTRYPOINT ["java"]  

