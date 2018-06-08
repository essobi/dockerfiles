FROM ubuntu:16.04  
MAINTAINER caotian <caotian@qq.com>  
  
env SHOP_PATH /var/www/shop  
  
# use chinese mirror for apt-update  
#RUN sed -i "s/archive.ubuntu.com/cn.archive.ubuntu.com/g"
/etc/apt/sources.list  
# install nginx, php  
RUN apt-get update \  
&& apt-get install -y supervisor nginx php7.0-fpm php7.0-mysql php7.0-common
php7.0-curl php7.0-opcache php7.0-mcrypt php7.0-mbstring \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/doc/*  
  
# copy nginx.conf shpo.conf  
RUN rm /etc/nginx/nginx.conf  
RUN ln -s $SHOP_PATH/data/conf/nginx.conf /etc/nginx/nginx.conf  
RUN rm /etc/nginx/sites-enabled/default  
RUN ln -s $SHOP_PATH/data/conf/shop.conf /etc/nginx/sites-enabled/shop  
  
# override php.ini  
RUN ln -s $SHOP_PATH/data/conf/php.ini
/etc/php/7.0/fpm/conf.d/99-overrides.ini  
  
# set php-fpm clear_env to no # not effected, disabled  
#RUN sed -i -e "s/;clear_env\s*=\s*no/clear_env = no/g"
/etc/php/7.0/fpm/pool.d/www.conf  
# change locale  
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime  
  
# expose https port 443  
EXPOSE 443  
#start script  
CMD chmod +x $SHOP_PATH/data/scripts/start.sh &&
$SHOP_PATH/data/scripts/start.sh

