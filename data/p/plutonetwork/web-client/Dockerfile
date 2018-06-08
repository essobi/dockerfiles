FROM ubuntu:14.04  
ENV NODE_VERSION='9'  
RUN apt update  
  
RUN apt-get install build-essential curl libssl-dev -y  
  
RUN curl -sL https://deb.nodesource.com/setup_${NODE_VERSION}.x | bash - \  
&& apt -y install build-essential \  
&& apt -y install nodejs \  
&& npm i -g npm  
  
RUN apt-get install -y zip gconf-service libasound2 libatk1.0-0 libc6
libcairo2 libcups2 libdbus-1-3 libexpat1 libfontconfig1 libgcc1 libgconf-2-4
libgdk-pixbuf2.0-0 libglib2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0
libpangocairo-1.0-0 libstdc++6 libx11-6 libx11-xcb1 libxcb1 libxcomposite1
libxcursor1 libxdamage1 libxext6 libxfixes3 libxi6 libxrandr2 libxrender1
libxss1 libxtst6 ca-certificates fonts-liberation libappindicator1 libnss3
lsb-release xdg-utils wget  
  
RUN apt-get autoclean  
  
RUN rm -rf node_modules && npm install  

