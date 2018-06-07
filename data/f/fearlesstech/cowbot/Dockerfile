FROM node:8-stretch  
  
  
# Get Google Chrome  
RUN apt-get update && apt-get install -y \  
wget && \  
wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key
add - && \  
echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' |
tee /etc/apt/sources.list.d/google-chrome.list && \  
apt-get update && \  
apt-get install -y \  
google-chrome-stable && \  
rm -rf /var/lib/apt/lists/*  
  
RUN mkdir /app  
WORKDIR /app  
  
RUN curl -o- -L https://yarnpkg.com/install.sh | bash  
  
COPY yarn.lock package.json ./  
RUN yarn install --frozen-lockfile --production && yarn cache clean  
  
COPY . .  
  
EXPOSE 3000  
CMD ["node", "app.js"]  

