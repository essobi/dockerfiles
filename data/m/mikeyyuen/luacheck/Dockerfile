FROM ubuntu:16.04  
RUN apt-get update -yqq && \  
apt-get install -yqq luarocks && \  
rm -rf /var/lib/apt/lists/* && \  
luarocks install luacheck && \  
mkdir -p /lua  
  
COPY luacheckrc /etc/luacheckrc  
  
WORKDIR /lua  
  
CMD [ "/usr/local/bin/luacheck", "--config", "/etc/luacheckrc", "/lua" ]  
  

