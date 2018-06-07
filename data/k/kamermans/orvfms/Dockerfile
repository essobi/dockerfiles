FROM phusion/baseimage:0.9.19  
ENV DEBIAN_FRONTEND noninteractive  
ENV TERM xterm  
  
RUN apt-get -y update \  
&& apt-get install -y \  
nginx \  
php7.0-cli \  
php7.0-fpm \  
htop \  
nano \  
git \  
&& apt-get -qy autoremove \  
&& apt-get clean \  
&& rm -r /var/lib/apt/lists/*  
  
RUN ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log \  
&& rm -f /etc/nginx/sites-enabled/* \  
&& echo '\n# Mitigate httpoxy attack\nfastcgi_param HTTP_PROXY "";' >>
/etc/nginx/fastcgi_params \  
&& cd /opt \  
&& git clone https://github.com/kamermans/orvfms.git \  
&& rm -rf orvfms/.git  
  
COPY resources/service /etc/service  
COPY resources/nginx/*.conf /etc/nginx/sites-enabled/  
COPY resources/php-fpm/php-fpm.conf /etc/php/7.0/fpm/  
COPY resources/php-fpm/pool.d/* /etc/php/7.0/fpm/pool.d/  
  
WORKDIR /opt/orvfms  
  
EXPOSE 80  

