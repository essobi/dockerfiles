FROM nginx  
MAINTAINER sinkcup <sinkcup@163.com>  
  
RUN apt-get update -qq  
RUN apt-get upgrade -y  
RUN apt-get install -y python-pip  
RUN pip install mkdocs  
RUN cd /usr/share/nginx/ && \  
mkdocs new portal  
WORKDIR /usr/share/nginx/portal  
RUN mkdocs build  
RUN rm -f /etc/nginx/conf.d/*  
ADD nginx/conf.d /etc/nginx/conf.d/  
RUN sed -i "s|#gzip on;|gzip on; etag off; server_tokens off; gzip_types *;|"
/etc/nginx/nginx.conf  

