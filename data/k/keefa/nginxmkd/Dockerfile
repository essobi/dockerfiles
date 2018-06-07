FROM nginx  
MAINTAINER keith a  
  
RUN apt-get update -qq  
RUN apt-get upgrade -y  
RUN apt-get install -y python-pip  
RUN pip install mkdocs  
RUN pip install mkdocs-material  
RUN cd /usr/share/nginx/html/ && \  
mkdocs new Product  
RUN cd /usr/share/nginx/html/Product && \  
mkdocs build  
RUN rm -f /etc/nginx/conf.d/*  
ADD mkdocs.conf /etc/nginx/conf.d/  
RUN sed -i "s|#gzip on;|gzip on; etag off; server_tokens off; gzip_types *;|"
/etc/nginx/nginx.conf

