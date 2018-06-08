FROM node:8  
MAINTAINER Gregoire MORPAIN <gm@predicsis.com>, mdouchement  
  
ENV NODE_ENV production  
ENV DOCKER_EXECUTION 1  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
ARG chromium_libs='gconf-service libasound2 libatk1.0-0 libc6 libcairo2
libcups2 libdbus-1-3 libexpat1 libfontconfig1 libgcc1 libgconf-2-4 libgdk-
pixbuf2.0-0 libglib2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0
libpangocairo-1.0-0 libstdc++6 libx11-6 libx11-xcb1 libxcb1 libxcomposite1
libxcursor1 libxdamage1 libxext6 libxfixes3 libxi6 libxrandr2 libxrender1
libxss1 libxtst6 ca-certificates fonts-liberation libappindicator1 libnss3
lsb-release xdg-utils'  
RUN apt-get update && apt-get install -y git ${chromium_libs} \--no-install-
recommends && rm -rf /var/lib/apt/lists/*  
  
COPY package.json /usr/src/app/  
RUN npm install  
COPY . /usr/src/app/  
  
EXPOSE 4005  
CMD ["node", "index.js"]  

