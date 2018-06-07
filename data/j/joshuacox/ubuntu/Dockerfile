FROM ubuntu:14.04  
MAINTAINER Josh Cox "josh at webhosting coop"  
ENV DOCKER_UBUNTU_UPDATED 20160808  
  
RUN echo 'APT::Install-Recommends 0;' >> /etc/apt/apt.conf.d/01norecommends \  
&& echo 'APT::Install-Suggests 0;' >> /etc/apt/apt.conf.d/01norecommends \  
&& apt-get update \  
&& apt-get install -y vim.tiny wget sudo net-tools ca-certificates \  
&& rm -rf /var/lib/apt/lists/* # 20150220  

