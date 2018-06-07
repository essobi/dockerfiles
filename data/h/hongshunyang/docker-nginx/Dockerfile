FROM hongshunyang/docker-alpine  
MAINTAINER Hongshun Yang<yanghongshun@outlook.com>  
  
RUN apk add --no-cache nginx \  
&& rm -rf /var/cache/apk/*  
  
COPY tmpl/_etc_nginx_nginx.conf.tmpl /etc/nginx/nginx.conf.tmpl  
  
RUN mkdir -p /run/nginx  
  
EXPOSE 80 443  
CMD
["dockerize","-template","/etc/nginx/nginx.conf.tmpl:/etc/nginx/nginx.conf","nginx",
"-g", "daemon off;"]  
  

