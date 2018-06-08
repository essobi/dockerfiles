# Nginx & ngx_lua  
# for  
# fuelPHP  
# Single host application  
#  
# docker run -itd -p 80:80 -p 443:443 -v <html-dir>:/var/www --link
[php5-fpmコンテナ]:php5-fpm --link [mysqlコンテナ]:mysql -e
"FUEL_ENV=[local|development|production|...]" zannenform/nginx-fuelphp  
  
FROM ubuntu:14.04  
MAINTAINER zanenform  
  
# Install Nginx.  
RUN apt-get -y update && apt-get upgrade -y && \  
apt-get install -y nginx-extras lua-nginx-redis && \  
apt-get clean && rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*  
  
# Nginx Config.  
RUN chown -R www-data:www-data /var/lib/nginx && \  
sed -i '1s/^/daemon off;\n/' /etc/nginx/nginx.conf && \  
sed -i '1s/^/env PHP5_FPM_PORT_9000_TCP_ADDR;\n/' /etc/nginx/nginx.conf && \  
sed -i '1s/^/env MYSQL_PORT_3306_TCP_ADDR;\n/' /etc/nginx/nginx.conf && \  
sed -i '1s/^/env MYSQL_PORT_3306_TCP_PORT;\n/' /etc/nginx/nginx.conf && \  
sed -i '1s/^/env FUEL_ENV;\n/' /etc/nginx/nginx.conf && \  
mkdir /var/www  
  
COPY fuelphp-conf /etc/nginx/sites-available/default  
  
# Define mountable directories.  
VOLUME ["/var/www"]  
  
# Expose ports.  
EXPOSE 80 443  
# Define default command.  
CMD ["/usr/sbin/nginx"]  

