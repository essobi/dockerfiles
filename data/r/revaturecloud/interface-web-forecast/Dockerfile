# STAGE - BUILD  
FROM node:carbon as build  
ARG ANGULAR_CLI=6.0.7  
WORKDIR /docker  
COPY . .  
RUN npm install  
RUN npm run build  
RUN npm install -g @angular/cli@${ANGULAR_CLI}  
ENTRYPOINT [ "ng" ]  
  
# STAGE - DEPLOY  
FROM nginx:1.14 as deploy  
ARG APP_VERSION=0.1.0  
LABEL app.version=${APP_VERSION}  
COPY \--from=build /docker/dist/interface-web-forecast /usr/share/nginx/html  
EXPOSE 80  

