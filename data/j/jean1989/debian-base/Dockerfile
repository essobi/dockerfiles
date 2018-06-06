FROM debian:jessie-slim  
  
MAINTAINER Jean1989  
  
ENV DEBIAN_FRONTEND="noninteractive"  
  
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-
selections \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends apt-utils \  
&& apt-get install -y --no-install-recommends wget \  
bash \  
ca-certificates \  
paxctl \  
tar \  
&& apt-get clean -y \  
&& apt-get autoclean -y \  
&& apt-get autoremove -y \  
&& rm -rf /usr/share/locale/* /var/cache/debconf/*-old /var/lib/apt/lists/* \  
/usr/share/doc/* /var/lib/apt/lists/*  

