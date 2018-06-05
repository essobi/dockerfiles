FROM node:8.4.0  
  
RUN export DEBIAN_FRONTEND=noninteractive LANG && \  
apt-get update && \  
apt-get install -y apt-utils && \  
apt-get install -y locales && \  
echo ja_JP.UTF-8 UTF-8 > /etc/locale.gen && \  
locale-gen ja_JP.UTF-8 && \  
update-locale LANG=ja_JP.UTF-8  
  
ENV LANG=ja_JP.UTF-8 \  
LANGUAGE=ja_JP.UTF-8 \  
LC_ALL=ja_JP.UTF-8 \  
NODE_PATH=/usr/local/lib/node_modules  
  
RUN npm install -g forever && \  
npm install -g eslint && \  
useradd -d /home/facegram -m -s /bin/bash facegram && \  
mkdir /usr/local/src/facegram && \  
chown facegram /usr/local/src/facegram && \  
chmod 755 /usr/local/src/facegram  
  
WORKDIR /usr/local/src/facegram  
COPY . ./  
RUN mkdir /usr/local/src/facegram/temp && \  
chmod 755 /usr/local/src/facegram/temp && \  
chown -R facegram:facegram .  
  
USER facegram  
  
RUN npm install  
  
CMD npm start  

