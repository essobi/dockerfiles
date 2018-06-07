FROM ubuntu:trusty  
  
MAINTAINER GaRaOne  
  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
RUN apt-get update && \  
apt-get install -y \  
apt-utils \  
software-properties-common \  
python-software-properties  
  
RUN add-apt-repository ppa:webupd8team/java -y && \  
apt-get update  
  
RUN echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-
set-selections  
RUN echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-
selections  
  
RUN apt-get update && \  
apt-get install -y \  
oracle-java8-installer \  
avahi-utils \  
curl \  
p7zip-full \  
maven \  
npm \  
nodejs-legacy  
  
# CLEAN CACHE  
RUN rm -rf /var/lib/apt/lists/*  
  
CMD ["/bin/bash"]  

