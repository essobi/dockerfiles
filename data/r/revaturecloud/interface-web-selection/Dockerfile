# STAGE - BUILD  
FROM node:carbon as build  
WORKDIR /docker  
COPY . .  
RUN npm install  
RUN npm run build  
  
# STAGE - DEPLOY  
FROM nginx:1.14 as deploy  
ARG APP_VERSION=0.1.0  
LABEL app.version=${APP_VERSION}  
COPY \--from=build /docker/dist/interface-web-selection /usr/share/nginx/html  
EXPOSE 80  

