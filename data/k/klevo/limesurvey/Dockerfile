FROM dockerfile/ubuntu  
  
# install required packages  
RUN apt-get update && \  
apt-get install -y \  
  
# php-fpm & nginx  
php5-mysql php5-fpm php5-gd nginx \  
  
# nullmailer for relaying emails  
nullmailer  
  
# download limesurvey  
RUN wget -O limesurvey.tar.bz2 http://www.limesurvey.org/en/stable-
release/finish/25-latest-stable-release/1207-limesurvey205plus-
build141210-tar-bz2  
  
RUN tar xjf limesurvey.tar.bz2 && \  
chown -R www-data:www-data limesurvey && \  
chmod -R 0777 limesurvey/tmp && \  
chmod -R 0777 limesurvey/upload && \  
chmod -R 0777 limesurvey/application/config && \  
# keep a copy, so the init script can use it  
cp -r limesurvey /srv/  
  
  
# Expose nginx  
EXPOSE 80  
VOLUME ["/srv/limesurvey/tmp", "/srv/limesurvey/upload",
"/srv/limesurvey/application/config"]  
  
ADD nullmailer/remotes /etc/nullmailer/remotes  
  
ADD php-fpm/www.conf /etc/php5/fpm/php-fpm.conf  
ADD nginx/default.conf /etc/nginx/sites-available/default  
  
ADD scripts/init_nullmailer /init_nullmailer  
ADD scripts/run_limesurvey /run_limesurvey  
  
CMD ["/run_limesurvey"]

