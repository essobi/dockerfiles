# Based on Kali Linux Rolling Distribution  
FROM kalilinux/kali-linux-docker  
LABEL MAINTAINER https://about.me/chihchun  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get -y update \  
&& apt-get dist-upgrade -y  
  
RUN apt-get -y build-dep metasploit-framework  
RUN cd /usr/local/src/ \  
&& git clone https://github.com/rapid7/metasploit-framework.git \  
&& cd metasploit-framework \  
&& bundle install \  
&& for MSF in $(ls msf*); do ln -s $PWD/$MSF /usr/local/bin/$MSF;done  
RUN apt-get install -y --no-install-recommends $(apt-cache depends metasploit-
framework | grep Depends | sed "s/.*ends:\ //" | tr '\n' ' ')  
CMD msfconsole  

