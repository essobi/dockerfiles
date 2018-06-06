FROM debian:8  
# install phppgadmin  
RUN DEBIAN_FRONTEND=noninteractive \  
apt update && \  
apt install -y php5-cli php5 php5-mcrypt php5-pgsql postgresql-contrib
phppgadmin  
  
# Activate a2enmod  
RUN a2enmod rewrite  
  
# Fix phppgadmin  
ADD ./phppgadmin.conf /etc/apache2/conf-available/phppgadmin.conf  
ADD ./config.inc.php /usr/share/phppgadmin/conf/config.inc.php  
RUN sed -i 's/variables_order = "GPCS"/variables_order = "EGPCS"/g'
/etc/php5/apache2/php.ini  
  
RUN a2enconf phppgadmin  
  
EXPOSE 80  
ADD start.sh /start.sh  
RUN chmod 0755 /start.sh  
CMD ["bash", "start.sh"]  
  

