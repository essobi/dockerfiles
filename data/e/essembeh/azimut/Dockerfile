FROM richarvey/nginx-php-fpm:latest  
MAINTAINER Sébastien M-B <seb@essembeh.org>  
  
RUN apt-get update  
RUN apt-get install -q -y --no-install-recommends \  
sqlite3 \  
&& apt-get clean  
  
RUN git clone https://github.com/essembeh/azimut /azimut  
RUN cd /azimut/www/cache && ./createDatabase.sh && cd -  
RUN chown -R www-data:www-data /azimut/www/  
  
RUN sed -i s@/usr/share/nginx/html@/azimut/www@g \  
/etc/nginx/*.conf /etc/nginx/*/*.conf  

