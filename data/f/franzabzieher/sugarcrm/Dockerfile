FROM phusion/baseimage  
MAINTAINER Franz Abzieher <franz@abzieher.net>  
  
RUN apt-get update && \  
apt-get install -y apache2 libapache2-mod-php5 php-apc php5-mysql php5-imap
php5-curl php5-gd php5-memcached curl python cron && \  
curl -SL
"http://switch.dl.sourceforge.net/project/sugarcrm/1%20-%20SugarCRM%206.5.X/SugarCommunityEdition-6.5.X/SugarCE-6.5.20.zip"|python
-c "import
zipfile,sys,StringIO;zipfile.ZipFile(StringIO.StringIO(sys.stdin.read())).extractall('/var/www/')"
&& \  
rm -rf /var/www/html && mv /var/www/SugarCE-Full-6.5.20 /var/www/html && \  
sed -i 's/^upload_max_filesize = 2M$/upload_max_filesize = 10M/'
/etc/php5/apache2/php.ini && \  
chown www-data:www-data -R /var/www/html && \  
chmod -R 0755 /var/www/html/cache && \  
echo 'date.timezone = UTC' >> /etc/php5/apache2/php.ini && \  
mkdir /etc/service/apache2  
  
ADD crons.conf /root/crons.conf  
ADD apache2.sh /etc/service/apache2/run  
  
RUN crontab /root/crons.conf  
  
EXPOSE 80  

