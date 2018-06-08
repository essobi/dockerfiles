FROM debian:stretch  
MAINTAINER Stefan Dimitrov <stefan@dimitrov.li>  
  
# Install autossh  
RUN export DEBIAN_FRONTEND='noninteractive' && \  
apt-get update -qq && \  
apt-get install -qqy --no-install-recommends autossh \  
$(apt-get -s dist-upgrade|awk '/^Inst.*ecurity/ {print $2}') &&\  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/*  
  
ADD docker-entrypoint.sh /usr/local/bin  
  
ENTRYPOINT [ "docker-entrypoint.sh" ]  

