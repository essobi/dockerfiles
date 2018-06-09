FROM node:latest  
  
RUN mkdir koor  
  
ADD . /koor  
WORKDIR /koor  
RUN npm install  
  
ENV APP_ID setYourAppId  
ENV MASTER_KEY setYourMasterKey  
ENV DATABASE_URI setMongoDBURI  
  
# ENV CLOUD_CODE_MAIN cloudCodePath  
# ENV PARSE_MOUNT mountPath  
EXPOSE 1337  
CMD [ "npm", "start" ]  

