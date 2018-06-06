FROM whiledo/ilias-base:latest  
MAINTAINER Kevin Krummenauer <kevin@whiledo.de>  
  
ENV httppath="http://localhost" \  
iliaspath="ilias" \  
timezone="Europe/Berlin" \  
clientid="myilias" \  
iliasmasterpassword="secret" \  
  
mysqlhost="127.0.0.1" \  
mysqluser="root" \  
mysqlpassword="my-secret-pw" \  
mysqldbname="ilias" \  
mysqlport="3306" \  
  
language="de" \  
  
initmysql="no" \  
initadminfirstname="John" \  
initadminlastname="Doe" \  
initadminemail="John.Doe@example.com" \  
initfeedbackemail="John.Doe@example.com"  
  
  
WORKDIR /data  
ADD resources /data/resources/configured  
  
  
RUN mkdir -p /var/www/html/ilias/data/myilias/css \  
&& mkdir -p /var/www/html/ilias/data/myilias/lm_data \  
&& mkdir -p /var/www/html/ilias/data/myilias/mobs \  
&& mkdir -p /var/www/html/ilias/data/myilias/usr_images \  
&& cp /data/resources/configured/ilias.ini.php /var/www/html/ilias \  
&& cp /data/resources/configured/client.ini.php
/var/www/html/ilias/data/myilias \  
&& chown -R www-data:www-data /var/www/html/ilias \  
&& chmod -R 775 /var/www/html/ilias/data \  
&& chmod 666 /var/www/html/ilias/ilias.ini.php \  
&& chmod 666 /var/www/html/ilias/data/myilias/client.ini.php \  
  
&& mkdir -p /opt/iliasdata/myilias/files \  
&& mkdir -p /opt/iliasdata/myilias/forum \  
&& mkdir -p /opt/iliasdata/myilias/lm_data \  
&& mkdir -p /opt/iliasdata/myilias/mail \  
&& chown -R www-data:www-data /opt/iliasdata \  
&& chmod -R 751 /opt/iliasdata \  
  
&& chown www-data:www-data /data/resources/configured/entrypoint.sh \  
&& chmod 751 /data/resources/configured/entrypoint.sh  
  
#run apache in foreground mode, otherwise docker would stop running image
directly after having started  
ENTRYPOINT ["/data/resources/configured/entrypoint.sh"]  
  
#now run with docker run -d -p 80:80 whiledo/ilias

