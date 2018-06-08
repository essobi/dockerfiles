FROM debian:jessie  
MAINTAINER johnwu "v.la@live.cn"  
RUN apt-key adv --keyserver hkp://pgp.mit.edu:80 --recv-keys 1ABFE185 \  
&& apt-get update \  
&& apt-get install --no-install-recommends --no-install-suggests -y wget sudo
net-tools ca-certificates unzip \  
&& rm -rf /var/lib/apt/lists/*

