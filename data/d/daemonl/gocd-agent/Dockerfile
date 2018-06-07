FROM phusion/baseimage:0.9.18  
# Copied From Aravind SV <arvind.sv@gmail.com>  
MAINTAINER Damien Whitten <damien@rebase.com.au>  
  
RUN rm -rf /etc/service/sshd /etc/my_init.d/00_regen_ssh_host_keys.sh  
RUN apt-get update && apt-get install -y \  
apt-transport-https \  
ca-certificates \  
curl \  
git \  
iptables \  
lxc \  
mercurial \  
openjdk-7-jre-headless \  
subversion \  
unzip  
  
ADD https://download.go.cd/binaries/16.3.0-3183/deb/go-agent-16.3.0-3183.deb
/tmp/go-agent.deb  
  
RUN groupadd -r go -g 998  
RUN useradd -r -u 998 -c "Go User" -g go -d /var/go -m -s /bin/bash go  
  
WORKDIR /tmp  
  
RUN dpkg -i /tmp/go-agent.deb \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN curl -sSL https://get.docker.com/ | sh  
  
RUN sed -i 's/DAEMON=Y/DAEMON=N/' /etc/default/go-agent  
  
RUN mkdir /etc/service/go-agent  
  
ADD go-agent-start.sh /etc/service/go-agent/run  
  
CMD ["/etc/service/go-agent/run"]  
  
RUN usermod -a -G docker go  
  
VOLUME /var/lib/docker  

