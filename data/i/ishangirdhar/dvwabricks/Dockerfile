#################################################################  
# Dockerfile to build DVWA & Bricks Application container images  
# Based on tutum/lamp:latest  
#################################################################  
FROM tutum/lamp:latest  
# File Author / Maintainer  
MAINTAINER Ishan Girdhar <ishan@ishangirdhar.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Clean the /app directory before copying/installing anything & Update the
repository sources list  
RUN rm -fr /app/* && \  
apt-get update && apt-get install -yqq wget unzip php5-curl php5-gd && \  
rm -rf /var/lib/apt/lists/*  
  
################################## BEGIN INSTALLATION
##############################  
RUN \  
# Downloading Latest Version Bricks 2.2 from SourceForge  
wget -O /bricks.zip
http://sourceforge.net/projects/owaspbricks/files/Tuivai%20-%202.2/OWASP%20Bricks%20-%20Tuivai.zip
&& \  
unzip /bricks.zip && \  
rm -rf /app/* && \  
mkdir -p /app/bricks /app/dvwa && \  
cp -r /bricks/* /app/bricks && \  
rm -rf /bricks && \  
find /app/bricks -name "*.php" | xargs -n1 sed -i "s/\r/\n/g" && \  
sed -i "s/^\$dbuser.*/\$dbuser = 'root';/" /app/bricks/LocalSettings.php && \  
sed -i "s/^\$dbpass.*/\$dbpass = '';/g" /app/bricks/LocalSettings.php && \  
sed -i 's/.*error_reporting.*/error_reporting(E_ALL ^ E_DEPRECATED);/'
/app/bricks/config/setup.php && \  
sed -i 's/.*error_reporting.*/error_reporting(E_ALL ^ E_DEPRECATED);/'
/app/bricks/includes/PHPReverseProxy.php && \  
sed -i 's/.*error_reporting.*/error_reporting(E_ALL ^ E_DEPRECATED);/'
/app/bricks/includes/MySQLHandler.php && \  
echo 'session.save_path = "/tmp"' >> /etc/php5/apache2/php.ini && \  
  
# Downloading Latest Version of DVWA 1.9 from Github  
wget -O /dvwa.zip https://github.com/RandomStorm/DVWA/archive/v1.9.zip && \  
unzip /dvwa.zip && \  
cp -r /DVWA-1.9/* /app/dvwa && \  
rm -rf /DVWA-1.9 && \  
sed -i "s/^\$_DVWA\\[ 'db_user' \\] = 'root'/\$_DVWA[ 'db_user' ] = 'admin'/g"
/app/dvwa/config/config.inc.php && \  
sed -i "s/^allow_url_include = Off/allow_url_include = On/g"
/etc/php5/apache2/php.ini && \  
chmod 777 /app/dvwa/hackable/uploads
/app/dvwa/external/phpids/0.6/lib/IDS/tmp/phpids_log.txt && \  
echo "sed -i \"s/p@ssw0rd/\$PASS/g\" /app/dvwa/config/config.inc.php" >>
/create_mysql_admin_user.sh && \  
echo 'session.save_path = "/tmp"' >> /etc/php5/apache2/php.ini  
#################################### INSTALLATION END
#############################  
# Expose the default port  
EXPOSE 80 3306  
  
# Set default Entrypoint  
CMD ["/run.sh"]  
  

