FROM tutum/lamp:latest  
MAINTAINER Nikolay Golub <nikolay.v.golub@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Preparation  
RUN rm -fr /app/* && \  
apt-get update && apt-get install -yqq wget unzip php5-curl && \  
rm -rf /var/lib/apt/lists/*  
  
# Deploy Bricks  
# - Download version 2.2  
# - copy to app folder  
# - set up Mysql credentials: root without password  
# - disable deprecation warnings  
RUN \  
wget -O /bricks.zip
http://sourceforge.net/projects/owaspbricks/files/Tuivai%20-%202.2/OWASP%20Bricks%20-%20Tuivai.zip
&& \  
unzip /bricks.zip && \  
rm -rf /app/* && \  
cp -r /bricks/* /app && \  
rm -rf /bricks && \  
find /app -name "*.php" | xargs -n1 sed -i "s/\r/\n/g" && \  
sed -i "s/^\$dbuser.*/\$dbuser = 'root';/" /app/LocalSettings.php && \  
sed -i "s/^\$dbpass.*/\$dbpass = '';/g" /app/LocalSettings.php && \  
sed -i 's/.*error_reporting.*/error_reporting(E_ALL ^ E_DEPRECATED);/'
/app/config/setup.php && \  
sed -i 's/.*error_reporting.*/error_reporting(E_ALL ^ E_DEPRECATED);/'
/app/includes/PHPReverseProxy.php && \  
sed -i 's/.*error_reporting.*/error_reporting(E_ALL ^ E_DEPRECATED);/'
/app/includes/MySQLHandler.php && \  
echo 'session.save_path = "/tmp"' >> /etc/php5/apache2/php.ini  
  
EXPOSE 80 3306  
CMD ["/run.sh"]  

