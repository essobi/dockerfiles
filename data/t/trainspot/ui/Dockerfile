### STAGE 1: Build ###  
# We label our stage as ‘builder’  
FROM node:8-alpine as builder  
  
COPY package.json .  
  
## Storing node modules on a separate layer will prevent unnecessary npm
installs at each build  
RUN npm i && mkdir /ng-app && cp -R ./node_modules ./ng-app  
  
WORKDIR /ng-app  
  
COPY . .  
  
## Build the angular app in production mode and store the artifacts in dist
folder  
RUN $(npm bin)/ng build --prod --env=prod  
  
### STAGE 2: Setup ###  
FROM nginx:1.13-alpine  
  
## Copy our default nginx config  
COPY nginx/default.conf /etc/nginx/conf.d/  
COPY run.sh /var/run/  
  
## Remove default nginx website  
RUN chmod 755 /var/run/run.sh && rm -rf /usr/share/nginx/html/*  
  
## From ‘builder’ stage copy over the artifacts in dist folder to default
nginx public folder  
COPY \--from=builder /ng-app/dist /usr/share/nginx/html  
#RUN chown -R 1057860000:1057860000 /usr/share/nginx/html /var/cache/nginx
/var/run  
WORKDIR /var/run  
  
EXPOSE 8081  
ENTRYPOINT ["./run.sh"]  

