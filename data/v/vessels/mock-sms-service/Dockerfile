FROM node:6  
# app directory  
ENV APP_DIR /usr/src/app  
  
# set config  
ENV NPM_CONFIG_LOGLEVEL warn  
  
RUN mkdir -p ${APP_DIR}  
WORKDIR ${APP_DIR}  
  
RUN npm install -g nodemon  
  
# install app dependencies  
ADD package.json ./  
RUN npm install  
  
COPY . ./  
  
EXPOSE 3001  
CMD ["nodemon", "index.js"]  

