FROM alpine:3.7 AS builder  
  
EXPOSE 80  
ENV NPM_CONFIG_PROGRESS=false \  
NPM_CONFIG_SPIN=false  
  
ARG BASE_HREF=/hxlpreview  
ARG BUILD_ENV=production  
  
WORKDIR /srv/hxlpreview  
  
COPY . .  
  
RUN apk add --update-cache \  
nodejs \  
nodejs-npm \  
git \  
curl \  
nano && \  
npm install -g @angular/cli && \  
npm install && \  
ng build --target=production --environment=$BUILD_ENV \--aot=false -bh
$BASE_HREF/ && \  
cp -a docker/default.conf dist && \  
sed -i "s%{{BASE_HREF}}%${BASE_HREF}%" dist/default.conf  
  
FROM alpine:3.6  
COPY \--from=builder /srv/hxlpreview/dist /var/www  
  
RUN apk add --update nginx && \  
mkdir -p /run/nginx && \  
mv /var/www/default.conf /etc/nginx/conf.d  
  
ENTRYPOINT ["nginx", "-g", "daemon off;"]  

