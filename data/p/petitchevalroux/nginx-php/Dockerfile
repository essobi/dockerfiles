FROM debian:wheezy  
MAINTAINER Patrick Poulain <docker@m41l.me>  
RUN apt-key adv --keyserver pgp.mit.edu --recv-keys
573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62  
RUN echo "deb http://nginx.org/packages/mainline/debian/ wheezy nginx" >>
/etc/apt/sources.list  
ENV NGINX_VERSION 1.7.6-1~wheezy  
RUN apt-get update && apt-get install -y nginx=${NGINX_VERSION}  
COPY ./nginx.conf /etc/nginx/nginx.conf  
RUN mkdir -p /var/www && \  
echo "Hello World !" > /var/www/index.html && \  
chown -R www-data:www-data /var/www  
RUN apt-get -y autoremove  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
EXPOSE 80  
CMD ["nginx"]  
COPY ./includes /etc/nginx/includes

