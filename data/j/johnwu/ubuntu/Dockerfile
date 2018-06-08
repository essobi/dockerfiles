FROM ubuntu:trusty-20160711  
MAINTAINER johnwu "v.la@live.cn"  
  
RUN echo 'APT::Install-Recommends 0;' >> /etc/apt/apt.conf.d/01norecommends \  
&& echo 'APT::Install-Suggests 0;' >> /etc/apt/apt.conf.d/01norecommends \  
&& apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y wget sudo net-tools ca-
certificates unzip iputils-ping \  
&& rm -rf /var/lib/apt/lists/*

