FROM node:slim  
  
WORKDIR /home/jsmtproxy  
  
RUN apt-get update && apt-get install -y git  
RUN git clone https://github.com/FreedomPrevails/JSMTProxy.git .  
  
RUN npm install pm2 -g  
  
EXPOSE 6969  
ARG MTPROTO_SECRET  
ENV MTPROTO_SECRET ${MTPROTO_SECRET:-DEADBEEFDEADBEEFDEADBEEF}  
RUN sed -i "s/b0cbcef5a486d9636472ac27f8e11a9d/${MTPROTO_SECRET}/g"
config.json  
  
CMD [ "pm2", "start", "mtproxy.js", "-i", "max"]  

