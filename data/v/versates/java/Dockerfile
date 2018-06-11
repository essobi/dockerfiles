FROM debian:jessie  
  
MAINTAINER Versates <docker@versates.com>  
  
ENV JAVA_INSTALLER="oracle-java8-installer" \  
JAVA_HOME="/usr/lib/jvm/java-8-oracle" \  
DEBIAN_FRONTEND=noninteractive DEBCONF_NONINTERACTIVE_SEEN=true  
  
RUN echo "${JAVA_INSTALLER}" shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections \  
&& echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" \  
> /etc/apt/sources.list.d/webupd8team-java.list \  
&& apt-key adv -q --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
EEA14886 \  
&& apt-get update -q \  
&& apt-get install -y -q "${JAVA_INSTALLER}" \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /var/cache/apt/* \  
&& rm -rf "/var/cache/${JAVA_INSTALLER}"  
  
CMD [ "bash" ]

