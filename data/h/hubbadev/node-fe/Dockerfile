FROM node:8  
RUN rm /usr/local/bin/yarn /usr/local/bin/yarnpkg && npm i -g yarn  
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add -  
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/
stable main" >> /etc/apt/sources.list.d/google.list'  
RUN apt-get update && apt-get install -y google-chrome-stable  

