FROM tuxotron/xvwa  
MAINTAINER xirax "bad-hombres"  
RUN true \  
&& export DEBIAN_FRONTEND=noninteractive \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends \  
php5-mcrypt \  
curl  
  
RUN php5enmod mcrypt  
RUN mv /var/www/html/xvwa /var/www/html/admin  
RUN find /var/www/html/admin -type f -exec sed -i 's/xvwa/admin/gi' {} +  
RUN find /var/www/html/admin -type f -exec sed -i 's/Xtreme vulnerable web
application/You didnt say the magic word/gi' {} +  
RUN echo "Boo!!" > /var/www/html/index.html  
RUN sed -i 's/xvwa;/admin;/gi' /create_xvwa_db.sh  
RUN mkdir -p /var/www/html/admin/img/uploads  
RUN chown -R www-data:www-data /var/www/html/admin/img  
ADD init_db.sh /init_db.sh  
ADD run.sh /run.sh  
RUN ./init_db.sh  
  
CMD [ "/run.sh" ]  

