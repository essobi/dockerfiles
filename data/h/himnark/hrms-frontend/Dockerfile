### STAGE 1: Build ###  
# We label our stage as ‘builder’  
FROM node:8.1.4-alpine as builder  
  
COPY package.json package-lock.json ./  
  
## Storing node modules on a separate layer will prevent unnecessary npm
installs at each build  
RUN npm i && mkdir /ng-app && cp -R ./node_modules ./ng-app  
  
WORKDIR /ng-app  
  
COPY . .  
  
## Build the angular app in production mode and store the artifacts in dist
folder  
RUN $(npm bin)/ng build --prod --env=prod  
  
### STAGE 2: Setup ###  
FROM nginx:stable-alpine-perl  
  
## Copy our default nginx config  
COPY nginx/default.conf /etc/nginx/conf.d/  
COPY nginx/nginx.conf /etc/nginx/  
COPY nginx/run.sh /etc/nginx/  
  
## Remove default nginx website  
RUN rm -rf /usr/share/nginx/html/*  
  
## From ‘builder’ stage copy over the artifacts in dist folder to default
nginx public folder  
COPY \--from=builder /ng-app/dist /usr/share/nginx/html  
  
CMD ["sh", "/etc/nginx/run.sh"]  

