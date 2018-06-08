FROM alpine:3.5  
LABEL maintainer "prajnamort@gmail.com"  
# python3, pip3  
RUN apk add \--no-cache python3  
  
# psycopg2 (pip3)  
RUN apk add \--no-cache postgresql-dev \  
&& apk add \--no-cache --virtual .psycopg2-deps gcc libc-dev python3-dev \  
&& pip3 install psycopg2==2.7.1 \  
&& apk del --no-cache .psycopg2-deps  
  
# py3-cryptography  
RUN apk add \--no-cache py3-cryptography  
  
# nginx  
RUN apk add \--no-cache nginx \  
&& rm /etc/nginx/conf.d/default.conf \  
&& mkdir /run/nginx  
  
# supervisor  
RUN apk add \--no-cache supervisor \  
&& mkdir -p /var/log/supervisor  

