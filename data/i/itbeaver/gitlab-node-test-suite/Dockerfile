FROM node:6.3  
MAINTAINER Alexander Bobrov, ITBeaver <al.bobrov@itbeaver.co>  
  
ENV NPM_CONFIG_LOGLEVEL info  
ENV DEBIAN_FRONTEND=noninteractive  
  
RUN apt-get update &&\  
apt-get install -y libgtk2.0-0 libgconf-2-4 \  
libasound2 libxtst6 libxss1 libnss3 xvfb  
  
COPY ./scripts/xvfb /etc/init.d/xvfb  
  
RUN /etc/init.d/xvfb start  

