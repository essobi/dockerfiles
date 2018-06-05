FROM phusion/baseimage  
CMD ["/sbin/my_init"]  
  
RUN apt-get update && apt-get install -y apache2 wget git-core php5  
RUN a2enmod rewrite  
  
#ModPagespeed  
RUN wget https://dl-ssl.google.com/dl/linux/direct/mod-pagespeed-
stable_current_amd64.deb  
RUN dpkg -i mod-pagespeed-*.deb && apt-get -f install -y && rm mod-pagespeed-*  
  
##Download the newest Monstra  
RUN rm -rf /var/www/ && \  
git clone https://github.com/Awilum/monstra-cms.git /var/www/ && \  
rm -rf /var/www/.git &&\  
chmod 775 /var/www/ -R  
  
##ADD Config Files  
ADD config/apache.conf /etc/apache2/sites-available/000-default.conf  
  
##Autostart Apache  
ADD /services/apache.sh /etc/my_init.d/apache.sh  
RUN chmod +x /etc/my_init.d/apache.sh  
  
VOLUME ["/var/www/storage","/var/www/public","/var/www/backups"]  
EXPOSE 80  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  

