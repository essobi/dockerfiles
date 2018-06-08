FROM nginx  
MAINTAINER Stefan Richter (https://github.com/sealor)  
  
ENV PHPMYADMIN_VERSION=4.5.1  
RUN apt-get update && \  
apt-get install -y curl php5-fpm php5-mysql && \  
curl
https://files.phpmyadmin.net/phpMyAdmin/${PHPMYADMIN_VERSION}/phpMyAdmin-${PHPMYADMIN_VERSION}-all-
languages.tar.gz | tar -C /usr/share/nginx/html -xz --strip 1 && \  
apt-get purge -y curl --auto-remove && \  
rm -rf /var/lib/apt/lists/*  
  
RUN usermod -aG www-data nginx  
  
RUN file=/etc/nginx/conf.d/default.conf && \  
sed -i 's/^}$//' $file && \  
sed -i 's/index index.html index.htm;/index index.php;/' $file && \  
echo '\t''location ~* \\.php {' >> $file && \  
echo '\t\t''include fastcgi_params;' >> $file && \  
echo '\t\t''fastcgi_pass unix:/var/run/php5-fpm.sock;' >> $file && \  
echo '\t\t''fastcgi_index index.php;' >> $file && \  
echo '\t\t''fastcgi_param SCRIPT_FILENAME
/usr/share/nginx/html/$fastcgi_script_name;' >> $file && \  
echo '\t''}' >> $file && \  
echo '}' >> $file  
  
RUN file=/usr/share/nginx/html/config.inc.php && \  
echo '<?php' > $file && \  
echo 'include "config.sample.inc.php";' >> $file && \  
echo '$cfg["Servers"][1]["host"] = "mysql";' >> $file && \  
echo '$cfg["Servers"][1]["AllowNoPassword"] = true;' >> $file && \  
echo '$file_with_secret = "config.inc.secret.php";' >> $file && \  
echo 'if (!file_exists($file_with_secret)) {' >> $file && \  
echo '\t''$secret = hash("sha512", openssl_random_pseudo_bytes(1000));' >>
$file && \  
echo '\t''file_put_contents($file_with_secret, "<?php
\$cfg[\"blowfish_secret\"] = \"$secret\"; ?>");' >> $file && \  
echo '}' >> $file && \  
echo 'include $file_with_secret;' >> $file && \  
echo '?>' >> $file  
  
CMD service php5-fpm start && nginx -g 'daemon off;'  

