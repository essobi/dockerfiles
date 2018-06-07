FROM ubuntu:16.04  
RUN apt-get update && \  
apt-get install -y --no-install-recommends software-properties-common ca-
certificates curl apt-transport-https && \  
apt-get dist-upgrade -y && \  
apt-get autoremove -y && \  
rm -rf /var/lib/apt/lists/*  
  
### gosu and entrypoint  
RUN gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 && \  
curl -o /usr/local/bin/gosu -SL
"https://github.com/tianon/gosu/releases/download/1.4/gosu-$(dpkg --print-
architecture)" && \  
curl -o /usr/local/bin/gosu.asc -SL
"https://github.com/tianon/gosu/releases/download/1.4/gosu-$(dpkg --print-
architecture).asc" && \  
gpg --verify /usr/local/bin/gosu.asc && \  
rm /usr/local/bin/gosu.asc && \  
chmod +x /usr/local/bin/gosu  
  
COPY entrypoint.sh /usr/local/bin/entrypoint.sh  
RUN chmod +x /usr/local/bin/entrypoint.sh  
  
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]  
###  

