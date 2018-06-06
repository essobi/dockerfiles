FROM buildpack-deps:jessie-scm  
  
MAINTAINER crazycode  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu precise main" |
tee /etc/apt/sources.list.d/webupd8team-java.list  
RUN echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu precise
main" | tee -a /etc/apt/sources.list.d/webupd8team-java.list  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886  
  
# Accept license  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections  
  
RUN apt-get update \  
&& apt-get install -y oracle-java8-installer \  
&& apt-get install -y oracle-java8-set-default  
  
# Cleanup test  
RUN apt-get -qq clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
/var/cache/oracle-jdk8-installer  
  
WORKDIR /root  
CMD ["/bin/bash"]  

