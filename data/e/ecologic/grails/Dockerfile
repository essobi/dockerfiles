FROM ubuntu:15.04  
MAINTAINER Markus Huggler <markus.huggler@ecologic.ch>  
  
RUN apt-get update && apt-get install -y git-core software-properties-common
curl unzip  
RUN add-apt-repository -y ppa:webupd8team/java  
RUN apt-get update  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -yq oracle-java8-installer  
  
# Install GVM  
RUN curl -s get.gvmtool.net | bash  
  
RUN ["/bin/bash", "-c", "source /root/.gvm/bin/gvm-init.sh"]  
RUN echo "gvm_suggestive_selfupdate=false" >> /root/.gvm/etc/config  
RUN ["/bin/bash", "-c", "-l", "gvm install grails 2.5.0"]  

