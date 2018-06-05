FROM debian:jessie  
  
# From https://hub.docker.com/r/nodesource/jessie-base/~/dockerfile/  
RUN apt-get update \  
&& apt-get install -y --force-yes --no-install-recommends\  
apt-transport-https \  
ssh-client \  
build-essential \  
curl \  
ca-certificates \  
git \  
lsb-release \  
python-all \  
rlwrap \  
&& rm -rf /var/lib/apt/lists/*;  
  
# From https://github.com/nodesource/docker-
node/blob/master/debian/jessie/node/5.0.0/Dockerfile  
RUN curl
https://deb.nodesource.com/node_5.x/pool/main/n/nodejs/nodejs_5.0.0-1nodesource1~jessie1_amd64.deb
> node.deb \  
&& dpkg -i node.deb \  
&& rm node.deb  
  
# Install gulp and bower globally  
RUN npm install -g gulp  
RUN npm install -g bower  
  
# Allow bower to run as root  
RUN echo '{ "allow_root": true, "interactive": false }' > ~/.bowerrc  
  
# Create directory for build  
RUN mkdir /build  
WORKDIR /build  
  
# Build Process  
COPY . .  
RUN npm install  
RUN bower install  
RUN gulp build  

