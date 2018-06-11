FROM ubuntu:14.04  
MAINTAINER Denis Wang <wangyg.personal@gmail.com>  
  
RUN echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-
set-selections  
RUN echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-
selections  
  
RUN apt-get update && \  
apt-get install -y \--no-install-recommends software-properties-common && \  
add-apt-repository ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y \--no-install-recommends oracle-java8-installer && \  
apt-get clean all && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
rm -rf /var/cache/oracle-jdk8-installer  
  

