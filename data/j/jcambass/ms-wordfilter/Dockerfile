FROM node:7.9-alpine  
  
ENV APP_HOME /srv/ms-wordfilter  
ENV PORT 3000  
RUN mkdir $APP_HOME  
  
WORKDIR $APP_HOME  
ADD . $APP_Home  
RUN npm install  
  
EXPOSE $PORT  
  
CMD ["node", "index.js"]  

