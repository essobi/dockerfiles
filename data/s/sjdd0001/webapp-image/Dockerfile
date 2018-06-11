FROM ubuntu-upstart  
MAINTAINER Sky.Y.Chen <chenyanhasmail@gmail.com>  
VOLUME ["/tmp/data"]  
RUN apt-get update  
RUN cd /opt && wget
https://nodejs.org/dist/v0.12.7/node-v0.12.7-linux-x64.tar.gz && tar -xzf
node-v0.12.7-linux-x64.tar.gz && rm -f node-v0.12.7-linux-x64.tar.gz && mv
node-v0.12.7-linux-x64 node  
RUN cd /usr/local/bin && ln -s /opt/node/bin/* .  
RUN npm install -g generator-keystone  
RUN mkdir -p /root/.config/configstore  
EXPOSE 3000  
WORKDIR /src  
CMD ["/bin/bash"]

