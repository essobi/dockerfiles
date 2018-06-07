FROM node:9  
WORKDIR /usr/src/app  
CMD [ "npm", "start" ]  
EXPOSE 3000  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \  
apt-transport-https \  
ca-certificates \  
curl \  
gnupg \  
&& curl -sSL https://dl.google.com/linux/linux_signing_key.pub \  
| apt-key add - \  
&& echo "deb [arch=amd64] https://dl.google.com/linux/chrome/deb/ stable main"
> /etc/apt/sources.list.d/google-chrome.list \  
&& apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \  
google-chrome-stable \  
&& rm -rf /var/lib/apt/lists/* \  
&& groupadd -r chrome \  
&& useradd -r -g chrome -G audio,video chrome \  
&& mkdir -p /home/chrome \  
&& chown -R chrome:chrome /home/chrome  
  
COPY package.json /usr/src/app/  
RUN npm install && npm cache clean --force  
COPY . /usr/src/app  
  
USER chrome  

