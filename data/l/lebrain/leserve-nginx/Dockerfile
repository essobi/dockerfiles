FROM nginx:alpine  
  
MAINTAINER Ilya Shtrikul <shtricul@gmail.com>  
  
ADD ./config/nginx.conf /etc/nginx/  
COPY ./sites/* /etc/nginx/sites-available/  
COPY ./config/other/*.conf /etc/nginx/conf.d/  
  
RUN apk update \  
&& apk upgrade \  
&& apk add --no-cache bash zsh \  
&& adduser -D -H -u 1000 -s /bin/bash www-data \  
&& rm /etc/nginx/conf.d/default.conf  
  
CMD ["nginx"]  
  
EXPOSE 80 443

