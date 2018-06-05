FROM java:8-jre  
MAINTAINER Li Lin <guru.lin@gmail.com>  
  
# install a few things that we'll need  
RUN apt-get update \  
&& apt-get install -y \  
telnet \  
p7zip \  
python-minimal \  
vim \  
xmlstarlet \  
&& rm -rf /var/lib/apt/lists/* \  
&& curl -o /usr/local/bin/gosu -Lks
https://github.com/tianon/gosu/releases/download/1.2/gosu-amd64 \  
&& curl -o /usr/local/bin/gosu.asc -sL
https://github.com/tianon/gosu/releases/download/1.2/gosu-amd64.asc \  
&& gpg --keyserver pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& gpg --verify /usr/local/bin/gosu.asc \  
&& rm /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu  
  
CMD ["/bin/bash", "--login"]  
  

