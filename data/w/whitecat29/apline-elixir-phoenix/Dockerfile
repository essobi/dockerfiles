FROM whitecat29/apline-elixir:latest  
MAINTAINER Willam Tran <chitran.whitecat@gmail.com>  
  
ENV TERM=xterm  
  
RUN \  
mkdir -p /opt/app && \  
chmod -R 777 /opt/app && \  
apk update && \  
apk --no-cache --update add \  
git make g++ wget curl inotify-tools freetype libpng libjpeg-turbo imagemagick
imagemagick-dev \  
nodejs nodejs-current-npm && \  
npm install npm -g --no-progress && \  
update-ca-certificates --fresh && \  
rm -rf /var/cache/apk/*  
  
# Add local node module binaries to PATH  
ENV PATH=./node_modules/.bin:$PATH \  
HOME=/opt/app  
  
# Install Hex+Rebar  
RUN mix local.hex --force && \  
mix local.rebar --force  
  
WORKDIR /opt/app  
  
CMD ["/bin/sh"]  

