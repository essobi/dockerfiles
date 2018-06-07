FROM ubuntu:14.04  
MAINTAINER Levin Keller <github@levinkeller.de>  
  
RUN apt-get update && apt-get upgrade -y && apt-get install -y \  
git \  
build-essential \  
bsdmainutils \  
libunbound-dev \  
libevent-dev \  
libgtest-dev \  
libboost1.55-all-dev \  
cmake  
  
COPY start.sh /scripts/start.sh  
  
COPY buildAndInstallMonero.sh /scripts/buildAndInstallMonero.sh  
  
RUN /scripts/buildAndInstallMonero.sh  
  
RUN apt-get purge -y \  
git \  
build-essential \  
bsdmainutils \  
libunbound-dev \  
libevent-dev \  
libgtest-dev \  
libboost1.55-all-dev \  
cmake  
  
VOLUME /monero  
  
EXPOSE 18080  
  
ENTRYPOINT ["/scripts/start.sh"]  
  

