FROM debian:jessie  
  
MAINTAINER Luis Ramos <momia191@gmail.com>  
  
# Install packages  
RUN apt-get update && \  
apt-get -y install pwgen python-setuptools curl git unzip && \  
apt-get install -y --force-yes --no-install-recommends\  
apt-transport-https \  
build-essential \  
ca-certificates \  
lsb-release \  
python-all \  
rlwrap \  
&& rm -rf /var/lib/apt/lists/*;  
  
RUN curl
https://deb.nodesource.com/iojs_1.x/pool/main/i/iojs/iojs_1.5.1-1nodesource1~jessie1_amd64.deb
> node.deb \  
&& dpkg -i node.deb \  
&& rm node.deb && \  
npm install -g pangyp\  
&& ln -s $(which pangyp) $(dirname $(which pangyp))/node-gyp\  
&& npm cache clear\  
&& node-gyp configure || echo "" && npm install -g chateau  
  
ADD config.js /config.js  
RUN chmod +x /config.js  
EXPOSE 9000  
CMD /bin/chateau -f /config.js  

