FROM ubuntu:trusty  
MAINTAINER Masato Morita <m.morita44@hotmail.com>  
  
ENV HELIX_VERSION 2017.1-1517929~trusty  
  
ADD https://package.perforce.com/perforce.pubkey /tmp/perforce.pubkey  
  
RUN apt-key add /tmp/perforce.pubkey && \  
echo "deb http://package.perforce.com/apt/ubuntu $(sed -n
's/^DISTRIB_CODENAME=\\(.*\\)$/\1/p' /etc/lsb-release) release" >
/etc/apt/sources.list.d/perforce.list && \  
rm /tmp/*  
  
RUN apt-get update && \  
apt-get install -y wget helix-swarm=$HELIX_VERSION helix-swarm-
triggers=$HELIX_VERSION  
  
ENV P4PORT perforce:1666  
ENV P4USER swarm  
ENV P4PASSWD swarm  
ENV MXHOST localhost  
  
EXPOSE 80 443  
ADD ./run.sh /  
  
CMD ["/run.sh"]  

