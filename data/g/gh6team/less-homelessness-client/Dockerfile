# Dockerfile (tag: v3)  
FROM node:6.8  
RUN mkdir /usr/src/app  
COPY . /usr/src/app  
WORKDIR /usr/src/app  
  
ENV NPM_CONFIG_LOGLEVEL warn  
RUN npm config set registry http://registry.npmjs.org/ && npm set
progress=false && npm install  
  
ENV NODE_ENV=production  
  
ENTRYPOINT [ "npm", "run", "build" ]  
EXPOSE 3000  

