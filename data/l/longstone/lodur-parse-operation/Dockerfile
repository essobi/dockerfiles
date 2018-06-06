FROM node:alpine  
EXPOSE 8080  
# copy app to src  
ADD . /script  
WORKDIR /script  
RUN npm install  
RUN npm run-script build  
ENV NODE_ENV=production  
ENTRYPOINT npm run-script start  
  

