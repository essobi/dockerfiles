# FROM webdevops/php-nginx  
FROM rossriley/docker-nginx-pg-php  
MAINTAINER Alan Acosta <zagato.gekko@gmail.com>  
  
LABEL "Proyecto de la clase Docker :: NGinx"  
  
RUN mkdir /var/www/public  
RUN echo '<?php echo "Conectado"; print_r( pg_connect("host=db port=5432
dbname=postgres user=postgres password=123456") ); ?>' >
/var/www/public/pg.php  
  
#RUN yum -y install vim gcc nano  
# COPY nano-2.3.1-10.el7.x86_64.rpm /root/  
#COPY vim-minimal-7.4.160-1.el7.x86_64.rpm /root  
# COPY apache2.conf /etc/apache2/sites-available/000-default.conf  
# RUN rpm -i /root/nano-2.3.1-10.el7.x86_64.rpm  
# RUN rpm -i /root/gcc*  
# CMD ""  

