FROM node AS build  
RUN chown -R node:node /usr/local/bin  
RUN chown -R node:node /usr/local/lib/node_modules  
USER node  
RUN npm install -g @angular/cli  
USER root  
WORKDIR /docker  
RUN ng new HelloNG  
WORKDIR /docker/HelloNG  
RUN ng build  
  
FROM nginx:1.12  
COPY \--from=build /docker/HelloNG/dist /usr/share/nginx/html  
EXPOSE 80  
# EXPOSE 80vagrant up  

