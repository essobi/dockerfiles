FROM ubuntu:16.04  
  
VOLUME /data  
RUN apt-get update \  
&& apt-get install -y sudo wget curl git vim gperf \  
flex bison libncurses5-dev gcc-arm-none-eabi python-pip python-pyelftools \  
&& groupadd -r mods && useradd -b /home -m -p SG5xasAtsa3VU -s /bin/bash -g
mods -G sudo mods \  
&& wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/1.10/gosu-amd64" \  
&& chmod +x /usr/local/bin/gosu  
USER mods  

