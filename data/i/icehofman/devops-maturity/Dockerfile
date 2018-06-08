### STAGE 1: Build ###  
FROM node:8.9.1-alpine as builder  
  
COPY package.json package-lock.json ./  
RUN npm set progress=false && npm config set depth 0 && npm cache clean
--force  
RUN npm i && mkdir /ng-app && cp -R ./node_modules ./ng-app  
  
WORKDIR /ng-app  
COPY . .  
  
RUN $(npm bin)/ng build --prod --build-optimizer  
  
### STAGE 2: Setup ###  
FROM nginx:1.13.7-alpine  
  
COPY nginx/default.conf /etc/nginx/conf.d/  
RUN rm -rf /usr/share/nginx/html/*  
COPY \--from=builder /ng-app/dist /usr/share/nginx/html  
  
EXPOSE 80  
CMD ["nginx", "-g", "daemon off;"]  

