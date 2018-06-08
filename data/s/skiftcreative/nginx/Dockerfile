FROM skiftcreative/gunicorn:3.4  
MAINTAINER Shawn McElroy <shawn@skift.io>  
  
RUN apk add --no-cache nginx && \  
rm -f /etc/nginx/nginx.conf  
  
ADD nginx.conf /etc/nginx/nginx.conf  
ADD supervisord.conf /etc/supervisor/conf.d/  
  
EXPOSE 80  

