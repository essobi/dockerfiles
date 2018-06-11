FROM debian:7.7  
MAINTAINER William Searle <will@livehybrid.com>  
  
RUN \  
export DEBIAN_FRONTEND=noninteractive && \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y unbound=1.4.17-3+deb7u2 && \  
apt-get clean && rm -rf /var/lib/apt/lists/*  
  
ADD unbound.conf /etc/unbound/unbound.conf  
# Add latest root-hints file  
ADD http://ftp.internic.net/domain/named.cache /etc/unbound/root.hints  
RUN chmod a+r /etc/unbound/root.hints  
EXPOSE 53  
ENTRYPOINT ["unbound"]  

