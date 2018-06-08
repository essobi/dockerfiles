FROM nginx:1.12-alpine-perl  
  
RUN apk add --no-cache --virtual nginx-deps \  
shadow && \  
groupadd -f -g 33 -o -r www-data && \  
useradd -b /var/www -d /var/www/html -g www-data -M -N -o -r -s /sbin/nologin
-u 33 www-data  
  
ARG LOGFILES="/var/log/nginx/access.log /var/log/nginx/error.log"  
ENV LOGFILES=$LOGFILES  
  
RUN rm -r /etc/nginx $LOGFILES || :  
  
COPY etc/nginx /etc/nginx  
COPY usr/local /usr/local  
COPY var/www/html /var/www/html  
  
ENTRYPOINT ["/usr/local/bin/logged-stdout"]  
  
EXPOSE 80  
CMD ["nginx", "-g", "daemon off;"]  

