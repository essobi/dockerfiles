FROM ubuntu:14.04  
# silence npm  
ENV NPM_CONFIG_LOGLEVEL warn  
  
# grab stuff to grab stuff  
RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" >
/etc/apt/sources.list && \  
apt-get update -qq && \  
apt-get install wget curl -qq -y  
  
# install node  
RUN curl -sL https://deb.nodesource.com/setup_5.x | bash - && \  
apt-get install -qq -y nodejs && \  
npm i npm@latest -g && \  
echo "Node: $(node -v)" && echo "NPM: $(npm -v)"  
  
# install overviewer  
RUN echo "deb http://overviewer.org/debian ./" >> /etc/apt/sources.list && \  
wget -O - http://overviewer.org/debian/overviewer.gpg.asc | apt-key add - && \  
apt-get update -qq && \  
apt-get install -qq -y minecraft-overviewer && \  
wget http://s3.amazonaws.com/Minecraft.Download/versions/1.9/1.9.jar -P
~/.minecraft/versions/1.9/  
  
# setup configuration directory  
RUN mkdir -p /etc/realmviewer  
COPY overviewer_config.py /etc/realmviewer/  
VOLUME /etc/realmviewer  
  
# Create app directory  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
# Install app  
COPY . /usr/src/app/  
RUN [ "npm", "install" ]  
  
# run app  
EXPOSE 80  
CMD [ "npm", "start" ]  

