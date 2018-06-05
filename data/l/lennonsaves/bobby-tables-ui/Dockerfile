FROM node:latest as build  
COPY . /app  
WORKDIR /app  
RUN npm install -p  
RUN npm run build  
  
FROM abiosoft/caddy  
COPY \--from=build /app/build /srv  
COPY Caddyfile /etc/Caddyfile

