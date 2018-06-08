# Builder  
FROM node:9.4 as builder  
  
WORKDIR /opt/web-client  
ADD . .  
  
RUN npm -g config set user root \  
&& npm install --loglevel=error -g @angular/cli \  
&& make setup \  
&& make lint \  
&& make build  
  
# Runtime  
FROM nginx:1.13-alpine  
  
RUN apk --no-cache add --upgrade nano \  
&& rm -rf /var/cache/apk/*  
  
COPY \--from=builder /opt/web-client/dist /usr/share/nginx/html/  
ADD nginx/ /etc/nginx/conf.d  
  
CMD sh /etc/nginx/conf.d/generate_env.sh && nginx -g 'daemon off;'  

