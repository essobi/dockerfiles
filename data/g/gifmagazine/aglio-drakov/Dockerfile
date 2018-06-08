FROM node:6.11-alpine  
  
RUN mkdir -p /run/nginx \  
&& apk --update --no-cache --virtual .build-deps add \  
make \  
g++ \  
python=2.7.12-r0 \  
&& apk --no-cache add \  
nginx \  
&& npm install -g --quiet --no-progress \  
aglio@2.3.0 \  
drakov@1.0.4 \  
&& npm cache clean --force \  
&& apk del .build-deps  
  
EXPOSE 80  
  
CMD ["nginx", "-g", "daemon off;"]  

