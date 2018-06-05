## -*- docker-image-name: "mcreations/gulp-bower" -*-  
FROM mcreations/openwrt-x64  
MAINTAINER Kambiz Darabi <darabi@m-creations.net>  
  
ADD image/root /  
  
RUN opkg update &&\  
opkg install nodejs nodejs-npm git git-http &&\  
rm /tmp/opkg-lists/* &&\  
npm install -g gulp bower npm-cache &&\  
mkdir /data &&\  
echo '{ "allow_root": true }' > /.bowerrc  
  
# npm and bower try to create dotfiles in $HOME  
ENV HOME /tmp  
  
WORKDIR /data  

