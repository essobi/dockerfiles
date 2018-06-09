FROM node:argon  
  
ENV APP_DIR "/usr/src/app"  
# create app directory  
RUN mkdir -p "$APP_DIR"  
WORKDIR "$APP_DIR"  
  
# install app dependencies  
COPY package.json "$APP_DIR/"  
RUN npm install  
  
# bundle app source  
COPY . "$APP_DIR"  
  
CMD [ "npm", "start" ]  
  
EXPOSE 1337

