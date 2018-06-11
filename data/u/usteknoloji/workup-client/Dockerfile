FROM node:6.9.2 as builder  
  
WORKDIR /ng-app  
  
RUN rm -rf ./node_modules  
  
RUN rm -rf ./dist  
  
COPY . .  
  
RUN npm rebuild node-sass --force  
  
RUN npm install  
  
RUN npm install typescript@'>=2.4.2 <2.7.0'  
  
RUN $(npm bin)/ng build -prod --aot  
  
FROM nginx:1.13  
COPY default.conf /etc/nginx/conf.d/  
  
## Remove default nginx website  
RUN rm -rf /usr/share/nginx/html/*  
  
## From 'builder' stage copy over the artifacts in dist folder to default
nginx public folder  
COPY \--from=builder /ng-app/dist /usr/share/nginx/html  
  
CMD ["nginx", "-g", "daemon off;"]

