FROM ubuntu  
  
MAINTAINER Niels Theen <werwofl@googlemail.com>  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y \  
php5 php5-pgsql php5-fpm php-apc php5-curl php5-cli supervisor ruby unzip
python wget nginx php5-sqlite php5-gd\  
&& apt-get clean  
  
# Get release 2.12 from the side  
ADD
https://github.com/SSilence/selfoss/releases/download/2.12/selfoss-2.12.zip
/selfoss-2.12.zip  
RUN unzip selfoss-2.12.zip -d /var/www  
  
WORKDIR /var/www  
  
# Make css writeable  
RUN chmod +rwx data/cache  
RUN chmod +rwx data/favicons  
RUN chmod +rwx data/logs  
RUN chmod +rwx data/thumbnails  
RUN chmod +rwx data/sqlite  
RUN chmod +rwx public  
RUN chmod +rwx index.php  
RUN cp defaults.ini config.ini  
RUN php update.php  
  
# add selfoss as the only nginx site  
ADD selfoss.nginx.conf /etc/nginx/sites-available/selfoss  
RUN ln -s /etc/nginx/sites-available/selfoss /etc/nginx/sites-enabled/selfoss  
RUN rm /etc/nginx/sites-enabled/default  
  
RUN chown www-data:www-data -R /var/www  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
CMD supervisord -c /etc/supervisor/conf.d/supervisord.conf  
  
EXPOSE 80  

