FROM nginx:mainline-alpine  
EXPOSE 80  
RUN mkdir /build \  
&& apk update \  
&& apk add --no-cache --virtual /build nginx php7-fpm php7-openssl php7-json  
  
COPY . /usr/share/nginx/html  
  
COPY nginx.conf /etc/nginx/nginx.conf  
  
RUN rm -rf /build && rm -rf /usr/share/nginx/html/nginx.conf
/usr/share/nginx/html/Dockerfile  
  
ENTRYPOINT php-fpm7 && nginx

