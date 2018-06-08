FROM ubuntu:trusty-20170602  
MAINTAINER zhouyq@goodrain.com  
  
# Timezone  
RUN echo "Asia/Shanghai" > /etc/timezone;dpkg-reconfigure -f noninteractive
tzdata  
  
ADD ./sources.list /etc/apt/sources.list  
  
RUN echo 'APT::Install-Recommends 0;' >> /etc/apt/apt.conf.d/01norecommends \  
&& echo 'APT::Install-Suggests 0;' >> /etc/apt/apt.conf.d/01norecommends \  
&& apt-get update \  
&& apt-get install -y vim.tiny wget sudo net-tools ca-certificates unzip apt-
transport-https \  
&& rm -rf /var/lib/apt/lists/* # 20150220  

