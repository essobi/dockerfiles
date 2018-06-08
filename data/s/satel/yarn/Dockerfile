FROM ubuntu:16.04  
ENV NODE_ENV building  
  
# Move to tmp  
WORKDIR /tmp  
  
# Install Dependancies  
RUN apt-get update && \  
apt-get install -y --force-yes --no-install-recommends \  
apt-transport-https \  
ssh-client \  
build-essential \  
curl \  
ca-certificates \  
git \  
libicu-dev \  
'libicu[0-9][0-9].*' \  
lsb-release \  
python-all \  
rlwrap \  
libelf1  
  
# Download and install Node  
RUN curl
https://deb.nodesource.com/node_6.x/pool/main/n/nodejs/nodejs_6.7.0-1nodesource1~xenial1_amd64.deb
> node.deb \  
&& dpkg -i node.deb \  
&& rm node.deb  
  
# Install PM2  
RUN npm install pm2 -g  
  
# Add yarn repository and install  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \  
echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list && \  
apt-get update && apt-get install -y \  
yarn  
  
# Nuke /tmp  
RUN rm -rf /tmp/*  

