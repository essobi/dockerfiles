FROM ubuntu:trusty-20150612  
MAINTAINER Mossuru777 mossuru777@gmail.com  
  
RUN sed -i -e
's@http://archive\\.ubuntu\\.com/@http://jp.archive.ubuntu.com/@g'
/etc/apt/sources.list \  
&& echo 'APT::Install-Recommends 0;' >> /etc/apt/apt.conf.d/01norecommends \  
&& echo 'APT::Install-Suggests 0;' >> /etc/apt/apt.conf.d/01norecommends \  
&& apt-get update \  
&& apt-get install -y vim.tiny wget sudo net-tools ca-certificates \  
&& rm -rf /var/lib/apt/lists/*  

