FROM ubuntu:14.04  
RUN locale-gen en_US.UTF-8  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv E56151BF && \  
echo deb http://repos.mesosphere.io/ubuntu trusty main >
/etc/apt/sources.list.d/mesosphere.list && \  
apt-get update && \  
apt-get -y install --no-install-recommends chronos mesos && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY entrypoint.sh /  
  
ENTRYPOINT ["/entrypoint.sh"]  

