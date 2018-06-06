# docker build -t epflsti/dockerpuppet .  
# docker run --rm epflsti/dockerpuppet --version  
FROM debian:stable-slim  
MAINTAINER STIIT Dev <stiitdev@groupes.epfl.ch>  
  
RUN apt update  
RUN apt install -y --no-install-recommends \  
ca-certificates \  
openssl \  
curl \  
ruby \  
util-linux \  
ipmitool \  
dmidecode \  
ethtool \  
iptables \  
snmp  
  
RUN apt-get autoremove && apt-get autoclean  
  
# gem search ^puppet$ --all  
RUN gem install -N \  
facter:'>= 2.4.6' \  
puppet:'= 3.8.7' \  
&& rm -fr /root/.gem  
  
ENV container docker  
VOLUME ["/sys/fs/cgroup", "/run", "/var/lib/puppet", "/lib64"]  
  
ENTRYPOINT ["/usr/local/bin/puppet"]  
CMD ["help"]  

