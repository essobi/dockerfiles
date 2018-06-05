# Base docker image  
FROM debian:stable-slim  
LABEL name="book-meter-feeder" \  
maintainer="Morimop <morimop@gmail.com>" \  
version="0.1" \  
description="bookmeter-feeder with Google Chrome Headless in a container"  
  
# Install deps + add Chrome Stable + purge all the things  
# Install Node.js(include npm), build-essential  
RUN apt-get update && apt-get install -y \  
curl \  
build-essential \  
apt-transport-https \  
ca-certificates \  
gnupg \  
\--no-install-recommends \  
&& curl -sSL https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key
add \- \  
&& curl -sL https://deb.nodesource.com/setup_8.x | bash - \  
&& apt-get install -y nodejs \  
&& curl -sSL https://dl.google.com/linux/linux_signing_key.pub | apt-key add
\- \  
&& echo "deb [arch=amd64] https://dl.google.com/linux/chrome/deb/ stable main"
> /etc/apt/sources.list.d/google-chrome.list \  
&& apt-get update && apt-get install -y \  
google-chrome-stable \  
\--no-install-recommends  
  
# Add Chrome as a user  
RUN groupadd -r chrome && useradd -r -g chrome -G audio,video chrome \  
&& mkdir -p /home/chrome && chown -R chrome:chrome /home/chrome  
  
# COPY module  
RUN mkdir /usr/local/node-app  
COPY package.json /usr/local/node-app/  
COPY index.js /usr/local/node-app/  
  
# Install python, build module(npm install)  
RUN apt-get update \  
&& apt-get install -y python2.7 \  
# && ln -s /usr/bin/python2.7 /usr/bin/python \  
&& cd /usr/local/node-app/ \  
&& npm install \  
&& apt-get purge --auto-remove -y curl gnupg \  
&& rm -rf /var/lib/apt/lists/*  

