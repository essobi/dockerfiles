FROM node:6.11.1  
# Install deps + add Chrome Stable + purge all the things  
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
\--no-install-recommends \  
&& rm -rf /var/lib/apt/lists/*  
  
# Add Chrome as a user  
# RUN groupadd -r chrome && useradd -r -g chrome -G audio,video chrome \  
# && mkdir -p /home/chrome && chown -R chrome:chrome /home/chrome  
# Run Chrome non-privileged  
# USER chrome  
# Point to correct chrome location  
ENV CHROME_PATH /usr/bin/google-chrome  
ENV PORT 9090  
EXPOSE 9090  
# Create app directory  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
# Install app dependencies  
COPY package.json /usr/src/app/  
RUN npm install  
  
# Bundle app source  
COPY . /usr/src/app  
  
CMD [ "npm", "start" ]  

