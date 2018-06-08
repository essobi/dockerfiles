FROM debian:jessie  
MAINTAINER https://github.com/cloneMe, Kelvin Chen <kelvin@kelvinchen.org>  
  
# Install all dependencies that are used in multiple images.  
RUN echo "deb http://httpredir.debian.org/debian jessie non-free" \  
>> /etc/apt/sources.list \  
&& apt-get update \  
&& apt-get install --no-install-recommends -y \  
vim \  
ca-certificates \  
python \  
python-dev \  
curl \  
git \  
nginx \  
unzip \  
unrar \  
supervisor \  
bzip2 \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN apt-get update \  
&& apt-get install --no-install-recommends -y apache2-utils \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
VOLUME /config  
  
EXPOSE 80 443  
ENV USE_SSL=false \  
server_name=localhost  
  
COPY start /  
  
COPY nginx/mime.types /etc/nginx/mime.types  
COPY nginx/nginx.conf /etc/nginx/nginx.conf  
COPY nginx/php.conf /etc/nginx/php.conf  
COPY nginx/proxy.conf /etc/nginx/proxy.conf  
COPY nginx/services.conf /etc/nginx/services.conf  
COPY nginx/htpasswd /etc/nginx/htpasswd  
COPY nginx/auth-basic.conf /etc/nginx/auth-basic.conf  
  
RUN rm -rf /var/www \  
&& mkdir /var/www  
COPY www /var/www/  
  
RUN chmod +x start  
CMD ["/start"]  

