# STAGE - BUILD  
FROM node:carbon as build  
WORKDIR /docker  
COPY . .  
RUN npm install -g @angular/cli@6.0.7  
RUN npm install  
RUN npm run build  
  
# STAGE - DEPLOY  
FROM nginx:1.14 as deploy  
COPY \--from=build /docker/dist/interface-web /usr/share/nginx/html  
EXPOSE 80  

