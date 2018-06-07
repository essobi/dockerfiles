FROM eboraas/apache-php  
MAINTAINER Dave Luo <kitsudo163@163.com>  
  
RUN apt-get update && apt-get -y install php5-memcache && apt-get clean && rm
-rf /var/lib/apt/lists/*  
ADD https://github.com/junstor/memadmin/archive/v1.0.12.tar.gz /var/www  
RUN rm -fr /var/www/html && ln -s /var/www/memadmin-1.0.12 /var/www/html && cd
/var/www/ && tar xvf v1.0.12.tar.gz  
  

