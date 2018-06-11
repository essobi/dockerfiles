FROM william17/nodejs-php-nginx:latest  
MAINTAINER William Leung<superbill2012@qq.com>  
  
RUN apt-get update && apt-get install -y supervisor  
  
VOLUME ["/data","/etc/supervisor/conf.d"]  
  
CMD ["/usr/bin/supervisord"]

