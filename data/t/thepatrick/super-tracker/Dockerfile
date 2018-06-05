FROM node:8-slim  
  
# Install latest chrome (dev) package.  
# Note: this also installs the necessary libs so we don't need the previous
RUN command.  
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add - &&\  
sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >>
/etc/apt/sources.list.d/google-chrome.list' &&\  
apt-get update &&\  
apt-get install -y google-chrome-unstable  
  
COPY package.json package-lock.json /app/  
  
WORKDIR /app  
  
RUN npm config set unsafe-perm true && npm install  
  
ENV TZ=Australia/Sydney  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone  
  
COPY . /app  
  
# CMD /bin/sh  
CMD node get.js  
  
# node --experimental-modules

