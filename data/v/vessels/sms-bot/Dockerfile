FROM node:6  
# app directory  
ENV APP_DIR /usr/src/app  
ENV TEST_DIR ${APP_DIR}/test  
ENV TOKEN .  
  
# set config  
ENV NPM_CONFIG_LOGLEVEL warn  
  
RUN mkdir -p ${APP_DIR}  
RUN mkdir -p ${TEST_DIR}  
WORKDIR ${APP_DIR}  
  
# install pm2 first  
RUN npm i -g pm2 mocha  
  
# install app dependencies  
ADD package.json ./  
RUN npm install  
  
# add the rest of the files  
ADD processes.json .  
ADD src/ ./src/  
  
EXPOSE 3000  
CMD ["pm2", "start", "processes.json", "--no-daemon"]  

