FROM tippiq/node-base:develop  
  
RUN \  
wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key
add - && \  
echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >>
/etc/apt/sources.list.d/google.list  
RUN \  
apt-get update && \  
apt-get install --no-install-recommends -y \  
google-chrome-stable \  
xvfb \  
&& \  
rm -rf /var/lib/apt/lists/*  
  
# use changes to package.json to force Docker not to use the cache  
# when we change our application's nodejs dependencies:  
WORKDIR /opt/app  
COPY package.json .  
RUN npm install  
  
VOLUME /opt/app/test-files  
  
COPY . .  
  
CMD npm start  

