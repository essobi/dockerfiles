FROM groventure/nagios-base:debian-jessie  
MAINTAINER Hellyna NG <hellyna@groventure.com>  
  
RUN export DEBIAN_FRONTEND='noninteractive' && \  
apt-get update && \  
apt-get install --no-install-recommends -y \  
nagios3-core && \  
apt-get autoremove -y && \  
apt-get clean -y && \  
rm -rvf /var/lib/apt/lists/* && \  
rm -rvf /var/tmp/* && \  
rm -rvf /tmp/*  
  
# /etc/nagios3 not included by default because web uses another group of
config  
VOLUME ["/var/lib/nagios3", "/var/log/nagios3", "/var/cache/nagios3"]  
WORKDIR /var/lib/nagios  
ENTRYPOINT ["/usr/sbin/nagios3", "/etc/nagios3/nagios.cfg"]  

