FROM tutum/lamp:latest  
MAINTAINER Alex M <originalsix@bluesand.org>  
#based on citizenstig/dvwa  
# override these on docker run command-line with -e  
ENV MYSQL_PASS u2ShallP@ss  
ENV CAPTCHA_PUB ""  
ENV CAPTCHA_PRIV ""  
ENV DEBIAN_FRONTEND noninteractive  
ENV CFGFILE /app/config/config.inc.php  
ENV APPVER 1.9  
# Preparation  
RUN \  
rm -fr /app/* && \  
apt-get update && apt-get install -yqq wget unzip php5-gd && \  
rm -rf /var/lib/apt/lists/* && \  
wget https://github.com/RandomStorm/DVWA/archive/v${APPVER}.zip && \  
unzip /v$APPVER.zip && \  
rm -rf app/* && \  
cp -r /DVWA-$APPVER/* /app && \  
rm -rf /DVWA-$APPVER && \  
sed -i "s/^\$_DVWA.*db_user.*=.*'root'.*$/\$_DVWA[ 'db_user' ] = 'admin';/"
$CFGFILE && \  
echo "sed -i \"s/p@ssw0rd/\$MYSQL_PASS/g\" $CFGFILE" >>
/create_mysql_admin_user.sh && \  
echo 'session.save_path = "/tmp"' >> /etc/php5/apache2/php.ini  
  
RUN \  
chmod 777 /app/hackable/uploads/ && \  
chmod 777 /app/external/phpids/0.6/lib/IDS/tmp/phpids_log.txt && \  
sed -i s/'captcha_pub.*'/"captcha_public_key' ] = getenv('CAPTCHA_PUB');"/
$CFGFILE && \  
sed -i s/'captcha_priv.*'/"captcha_private_key' ] = getenv('CAPTCHA_PRIV');"/
$CFGFILE  
  
EXPOSE 80 3306  
CMD ["/run.sh"]  

