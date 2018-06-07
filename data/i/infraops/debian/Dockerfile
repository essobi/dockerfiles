FROM debian:jessie  
MAINTAINER anderson@infraops.info  
  
RUN echo 'deb http://ftp.debian.org/debian jessie-backports main' >>
/etc/apt/sources.list  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update \  
&& apt-get -qqy install wget curl ca-certificates tzdata \  
nano wget rsyslog locales software-properties-common gosu --no-install-
recommends  
  
RUN cd /usr/local/bin \  
&& curl -sL $(curl -s
https://api.github.com/repos/jwilder/dockerize/releases/latest \  
| grep -E 'browser_.*amd64' | cut -d\" -f4) | tar xzv \  
&& chmod +x dockerize \  
&& apt-get clean && rm -rf /var/lib/apt/lists/*  
  
env TIMEZONE=America/Sao_Paulo  
RUN echo $TIMEZONE > /etc/timezone \  
&& dpkg-reconfigure -f noninteractive tzdata \  
&& sed -i 's/^# *\\(pt_BR.UTF-8\\)/\1/' /etc/locale.gen \  
&& locale-gen pt_BR.UTF8  
  
env LANG=pt_BR.UTF8  
env LANGUAGE=pt_BR.UTF8  
env LC_ALL=pt_BR.UTF8  
  
CMD ["/bin/bash"]  

