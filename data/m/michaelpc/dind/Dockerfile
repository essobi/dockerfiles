FROM michaelpc/perl-base:latest  
  
RUN apt-get update -qq && apt-get install -qqy \  
apt-transport-https \  
ca-certificates \  
curl \  
lxc \  
iptables  
  
RUN curl -sSL https://get.docker.com/ | sh  
  
ADD ./modules.dep.bin /lib/modules/4.4.0-57-generic/modules.dep.bin  
  
VOLUME /var/lib/docker  
  
ENV INITD_START_DOCKER docker  

