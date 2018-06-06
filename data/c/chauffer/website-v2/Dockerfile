FROM nginx:1.13-alpine  
  
WORKDIR /app  
COPY . /app  
  
RUN apk add --no-cache --virtual=.build-deps curl && \  
cd /tmp && \  
curl -L
https://github.com/gohugoio/hugo/releases/download/v0.40.2/hugo_0.40.2_linux-64bit.tar.gz
| tar -xz && \  
cd /app && \  
/tmp/hugo --destination=/usr/share/nginx/html && \  
rm -rf /tmp && \  
apk del .build-deps  
  
COPY simone.conf /etc/nginx/conf.d/default.conf  

