# Nginx & ngx_lua  
# Purpose  
# Multi host application  
# fuelPHP  
#  
# Require  
# redis  
#  
# redis と連携することでマルチホストアプリケーションサーバーに対応します。  
# docker run -itd -p 80:80 -p 443:443 --env REDISSERVER=[redis.の.IP.アドレス]
nginx  
  
FROM ubuntu:14.04  
MAINTAINER zanenform  
  
# Install Nginx.  
RUN apt-get -y update && apt-get install -y nginx-extras lua-nginx-redis  
  
# Nginx Config.  
RUN sed -i '1s/^/daemon off;\n/' /etc/nginx/nginx.conf && \  
sed -i '1s/^/env REDISSERVER;\n/' /etc/nginx/nginx.conf  
COPY fuelphp-conf /etc/nginx/sites-available/default  
# Install Redis cli.  
RUN apt-get install -y redis-tools  
  
# Expose ports.  
EXPOSE 80 443  
# Define default command.  
CMD ["/usr/sbin/nginx"]  

