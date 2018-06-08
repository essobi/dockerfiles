FROM node:6  
RUN mkdir -p /parse  
  
ADD package.json /parse  
ADD jsconfig.json /parse  
  
WORKDIR /parse  
  
RUN npm install  
  
ADD index.js /parse  
  
## ENV  
#ENV APP_ID myAppId  
#ENV MASTER_KEY myMasterKey  
#ENV DATABASE_URI mongodb://localhost:27017/dev  
#ENV CLOUD_CODE_MAIN ${CLOUD_CODE_HOME}/main.js  
#ENV PARSE_MOUNT /parse  
#ENV COLLECTION_PREFIX  
#ENV CLIENT_KEY  
#ENV REST_API_KEY  
#ENV DOTNET_KEY  
#ENV JAVASCRIPT_KEY  
#ENV DOTNET_KEY  
#ENV FILE_KEY  
#ENV FACEBOOK_APP_IDS "xx,xxx"  
#ENV SERVER_URL  
#ENV MAX_UPLOAD_SIZE  
EXPOSE 1337  
ENV NODE_PATH .  
  
CMD ["npm", "start"]  

