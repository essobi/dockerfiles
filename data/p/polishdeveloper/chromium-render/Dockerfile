FROM debian:stretch  
  
RUN apt-get update && apt-get install -y sudo curl git chromium gconf-service
gnupg2  
RUN curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -  
#RUN apt-get update && apt-get install -y nodejs sudo git chromium gconf-
service wget && rm -rf /var/lib/apt/lists/*  
RUN apt-get install -y nodejs  
RUN cd /srv && git clone
https://gerrit.wikimedia.org/r/mediawiki/services/chromium-render && cd
/srv/chromium-render && PUPPETEER_SKIP_CHROMIUM_DOWNLOAD=1 npm install  
RUN sed -i "s|{ args: puppeteerFlags }|{executablePath: '/usr/bin/chromium',
args: puppeteerFlags }|g" /srv/chromium-render/lib/renderer.js  
EXPOSE 3030  
WORKDIR /srv/chromium-render  
CMD [ "npm", "start"]  

