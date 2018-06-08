## Version 1.0.0  
FROM fortytwoio/base  
MAINTAINER Thomas Fritz <thomas.fritz@forty-two.io>  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -qqy --no-install-
recommends nginx-light > /dev/null 2>&1  
  
ADD ./etc/nginx/nginx.conf.tpl /etc/nginx/nginx.conf.tpl  
ADD ./etc/nginx/sites-enabled/default /etc/nginx/sites-enabled/default  
ADD ./index.html /srv/www/index.html  
  
ONBUILD ADD ./etc/nginx/sites-enabled/ /etc/nginx/sites-enabled/  
  
VOLUME ["/srv/www/"]  
  
EXPOSE 80  

