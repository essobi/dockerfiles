FROM node:latest  
  
LABEL com.buzz.tv.version="0.0.1-beta"  
LABEL vendor="EZYY Incorporated"  
LABEL com.buzz.tv.release-date="2015-02-12"  
LABEL com.buzz.tv.version.is-production=""  
  
ENV BUZZ_TV_VERSION 0.0.1-beta  
  
# Electron support (from: http://askubuntu.com/a/510186)  
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add - && \  
sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable
main" >> /etc/apt/sources.list.d/google-chrome.list' && \  
apt-get update -y && \  
apt-get install -y google-chrome-stable xvfb  
  
WORKDIR /usr/src/app  
  
COPY package.json .  
  
COPY yarn.lock .  
  
RUN yarn install  
  
COPY . .  
  
CMD ["yarn","run","dev"]  

