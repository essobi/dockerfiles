FROM node:6.10  
ENV APP_DIR /usr/src/app  
RUN mkdir -p ${APP_DIR}  
WORKDIR ${APP_DIR}  
  
# set config  
ENV NPM_CONFIG_LOGLEVEL warn  
  
RUN npm install -g nodemon webpack  
  
COPY package.json ./  
RUN npm install  
  
COPY ./ ./  
  
EXPOSE 3002  
#Webpack needs this defined for its build step  
ENV SMS_BOT_BASE_URL="https://sms.vesselstech.com"  
RUN npm run build  
# RUN cat dist/bundle.js | grep 'TEST_ENV'  
CMD ["./entrypoint.sh"]  

