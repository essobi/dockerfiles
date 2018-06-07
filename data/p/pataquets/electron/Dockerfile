FROM node  
  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get -y install \  
libasound2 \  
libgconf2-4 \  
libgtk2.0-0 \  
libnss3 \  
libx11-xcb1 \  
libxss1 \  
libxtst6 \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/  
  
WORKDIR /usr/src/app/  
RUN \  
mkdir -vp /usr/src/app/ && \  
chown -v node:node /usr/src/app/  
  
USER node  
RUN npm install electron  
  
ENTRYPOINT [ "npm", "start" ]  

