# docker build -t local-repo/gitlab-node-image:latest .  
  
FROM node:8  
  
RUN set -xe \  
&& wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add \- \  
&& sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable
main" >> /etc/apt/sources.list.d/google-chrome.list' \  
&& apt-get update \  
&& apt-get -y install google-chrome-stable

