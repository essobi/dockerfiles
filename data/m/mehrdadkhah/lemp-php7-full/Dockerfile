FROM mehrdadkhah/php7:ffmpeg  
  
MAINTAINER Mehrdad Dadkhah <mehrdad@dadkhah.me>  
  
ENV fpm_conf /usr/local/etc/php-fpm.d/www.conf  
  
RUN apt-get update -y && \  
apt-get install -y nginx && \  
apt-get install -y supervisor  
  
RUN mkdir -p /etc/nginx/sites-enabled/ && \  
rm -Rf /var/www/* && \  
mkdir /var/www/html/ && \  
rm -Rf /etc/nginx/sites-enabled/*  
  
RUN mkdir -p /var/log/supervisor  
  
# Copy our config  
RUN rm -Rf /etc/nginx/nginx.conf  
COPY ./nginx.conf /etc/nginx/nginx.conf  
COPY ./supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
COPY ./www.conf /usr/local/etc/php-fpm.d/  
COPY ./zz-docker.conf /usr/local/etc/php-fpm.d/  
  
WORKDIR /var/www/html  
  
RUN chown -R www-data:www-data .  
  
RUN rm -rf /var/lib/apt/lists/*  
  
EXPOSE 80 443  
CMD ["/usr/bin/supervisord", "-n", "-c",
"/etc/supervisor/conf.d/supervisord.conf"]

