FROM ubuntu:latest  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" |
tee -a /etc/apt/sources.list  
RUN echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty
main" | tee -a /etc/apt/sources.list  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886 \  
&& apt-get update && apt-get dist-upgrade -y \  
&& apt-get install -y git git-core wget curl zip unzip \  
&& apt-get install -y oracle-java8-installer ca-certificates \  
&& apt-get autoclean && apt-get --purge -y autoremove && rm -rf
/var/lib/apt/lists/* /tmp/* /var/tmp/*  

