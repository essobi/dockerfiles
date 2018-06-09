# Dockerfile  
FROM node:8-alpine  
  
WORKDIR /usr/src/app  
  
COPY package.json .  
  
RUN npm install  
  
# Bundle app source  
COPY . .  
  
ENV WEBSITE_LOCALE fr  
ENV GA_ID UA-110928879-2  
RUN npm run build  
  
EXPOSE 3000  
CMD [ "npm", "run", "prod" ]  

