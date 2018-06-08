FROM resin/armv7hf-debian:jessie  
  
RUN curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -  
  
RUN apt-get update && apt-get install -y \  
build-essential \  
fswebcam \  
git \  
nodejs \  
python-pip  
  
RUN pip install -U pip  
  
RUN pip install -U \  
platformio  
  
  
  
###################### Platform IO ############################  
  
WORKDIR /platformio  
  
RUN platformio init -d .  
RUN platformio lib install https://github.com/lunchbox-
lambda/firmata.git#1.0.0  
RUN rm -rf /platformio/src && ln -s
/platformio/.piolibdeps/LunchboxFirmata/src /platformio  
  
  
  
####################### Application ###########################  
  
ARG BUILD_VERSION  
  
WORKDIR /app  
  
ENV NODE_ENV=production  
ENV NODE_PATH=/app/node_modules/@lunchbox/brain/dist  
RUN npm install @lunchbox/brain@${BUILD_VERSION}  
RUN ln -s /app/node_modules/@lunchbox/brain/node_modules/@lunchbox/node-red
/node-red  
RUN echo "require('@lunchbox/brain')" >> index.js  
  
VOLUME /data  
  
EXPOSE 80  
  
  
  
################### Environment & Startup ######################  
  
WORKDIR /  
  
ENV LBOX_VERSION=${BUILD_VERSION}  
ENV DEBUG="backend:*, firmware:*, kernel:*, webapi:*, lib:*, service:*"  
  
RUN echo "#!/bin/bash" >> /start.sh && \  
echo "node /app |& tee /data/stdout.log" >> /start.sh  
  
RUN chmod 755 /start.sh  
  
CMD /start.sh  

