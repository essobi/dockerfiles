FROM alpine:3.7 AS builder  
  
ENV NPM_CONFIG_PROGRESS=false \  
NPM_CONFIG_SPIN=false  
  
WORKDIR /srv/wizard  
  
COPY . .  
  
RUN apk add --update-cache \  
nodejs \  
nodejs-npm \  
git \  
curl \  
nano && \  
npm install -g @angular/cli && \  
npm install && \  
ng build --prod -bh /wizard/quickcharts/  
  
FROM alpine:3.6  
RUN apk add --update nginx && \  
mkdir -p /run/nginx  
  
COPY ./docker/default.conf /etc/nginx/conf.d/  
COPY \--from=builder /srv/wizard/dist /var/www  
  
EXPOSE 80  
ENTRYPOINT ["nginx", "-g", "daemon off;"]  

