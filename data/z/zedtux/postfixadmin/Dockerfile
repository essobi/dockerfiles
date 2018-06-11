FROM corbinu/docker-nginx-php  
MAINTAINER Guillaume Hain zedtux@zedroot.org  
  
ENV POSTFIXADMIN_VERSION 2.92  
ENV POSTFIXADMIN_BASE_URL
http://downloads.sourceforge.net/project/postfixadmin/postfixadmin  
ENV APPLICATION_PATH /www  
ENV MYSQL_DB_NAME postfixadmin  
ENV MYSQL_DB_USERNAME postfixadmin  
  
# 1. Install mysql command to create MySQL database and user in case is
missing  
# 2. Download specific project version  
# 3. Extract the downloaded archive, move it to the APPLICATION_PATH and
remove  
# the archive  
# 4. Run composer to install dependencies  
# 5. Force permissions on var/ application folder as requested by
documentation  
# 6. Forward NGINX request and error logs to docker log collector  
RUN apt-get update && \  
apt-get install -y mysql-client-core-5.6 php5-imap && \  
wget
"$POSTFIXADMIN_BASE_URL/postfixadmin-$POSTFIXADMIN_VERSION/postfixadmin-$POSTFIXADMIN_VERSION.tar.gz"
&& \  
tar -xzf "postfixadmin-$POSTFIXADMIN_VERSION.tar.gz" && \  
rm "postfixadmin-$POSTFIXADMIN_VERSION.tar.gz" && \  
mv "postfixadmin-$POSTFIXADMIN_VERSION"/* $APPLICATION_PATH && \  
rm -rf "postfixadmin-$POSTFIXADMIN_VERSION/" && \  
chown www-data:www-data -R "$APPLICATION_PATH" && \  
ln -sf /dev/stdout /var/log/nginx/access.log && \  
ln -sf /dev/stderr /var/log/nginx/error.log  
  
# Add Postfix.Admin configuration file  
ADD etc/config.inc.php /www/config.inc.php  
  
# Add the run script  
ADD bin/run /usr/local/bin/run  
  
WORKDIR /www  
EXPOSE 80  
CMD ["/usr/local/bin/run"]  

