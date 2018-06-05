FROM node:8.4  
ENV NODE_ENV production  
ENV NPM_CONFIG_PRODUCTION false  
WORKDIR /app  
ADD . /app  
RUN npm install  
RUN npm run build:elm  
RUN npm run build  
ENV NPM_CONFIG_PRODUCTION true  
EXPOSE 5000

