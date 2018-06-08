# Docker file to run basic dev-env for CI  
FROM node:8.11.2  
LABEL maintainer="Simon Young <simon180@mac.com>"  
  
# Install Yarn  
RUN npm install -g yarn  
  
# Install chrome  
#RUN wget https://dl.google.com/linux/direct/google-chrome-
stable_current_amd64.deb && \  
# dpkg -i google-chrome-stable_current_amd64.deb; apt-get -fy install  
RUN apt-get update && apt-get install -y \  
apt-transport-https \  
ca-certificates \  
curl \  
gnupg \  
\--no-install-recommends \  
&& curl -sSL https://dl.google.com/linux/linux_signing_key.pub | apt-key add -
\  
&& echo "deb [arch=amd64] https://dl.google.com/linux/chrome/deb/ stable main"
> /etc/apt/sources.list.d/google-chrome.list \  
&& apt-get update && apt-get install -y \  
google-chrome-stable \  
\--no-install-recommends  
  
ENV CHROME_BIN=/usr/bin/google-chrome  
  
# Setup chromium  
RUN apt-get -qq update && apt-get install -y chromium  

