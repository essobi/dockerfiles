FROM ubuntu:16.04  
RUN apt-get update && apt-get install -y wget xz-utils tzdata  
  
RUN wget https://nodejs.org/dist/v6.11.0/node-v6.11.0-linux-x64.tar.xz  
RUN tar -C /usr/local \--strip-components 1 -xf node-v6.11.0-linux-x64.tar.xz
&& rm node-v6.11.0-linux-x64.tar.xz  
  
ENV NODE_HOME=/usr/local  
RUN npm install npm@5.1.0 && rm -rf /usr/local/lib/node_modules/npm && mv
node_modules/npm /usr/local/lib/node_modules/npm  
  
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add -  
RUN echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main"
>> /etc/apt/sources.list.d/google-chrome.list  
RUN apt-get update && apt-get install -y --no-install-recommends google-
chrome-stable  

