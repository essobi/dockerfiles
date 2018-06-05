FROM teodorescuserban/atman-base:latest  
  
MAINTAINER Serban Teodorescu, teodorescu.serban@gmail.com  
#ENV DEBIAN_FRONTEND noninteractive  
#RUN locale-gen en_US.UTF-8  
#ENV LANG en_US.UTF-8  
#ENV LANGUAGE en_US:en  
#ENV LC_ALL en_US.UTF-8  
  
RUN apt-get -qq -y update  
  
RUN apt-get install -qq -y \  
postfix \  
postfix-pcre \  
opendkim \  
opendkim-tools  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  

