FROM node as build  
RUN chown -R node:node /usr/local/lib/node_modules  
RUN chown -R node:node /usr/local/bin  
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

