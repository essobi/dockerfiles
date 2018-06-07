FROM node:boron  
RUN apt-get update  
RUN apt-get install libav-tools -y  
ENV APP_DIR /opt/impartus/xcoderservice  
RUN mkdir -p ${APP_DIR}  
WORKDIR ${APP_DIR}  
COPY package.json ${APP_DIR}  
RUN npm install  
COPY src ${APP_DIR}  
ENTRYPOINT ["node","app.js"]

