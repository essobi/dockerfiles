FROM alpine:latest  
  
  
# Download and instsall dependencies  
RUN apk --no-cache add postgresql nginx ca-certificates wget curl \  
php7-cli php7-curl php7-mcrypt php7-apcu php7-fpm \  
php7-sqlite3 php7-json php7-phar php7-iconv php7 \  
php7-mbstring php7-xml php7-fileinfo php7-openssl \  
php7-dom php7-tokenizer php7-ctype php7-pdo php7-pgsql \  
php7-pdo_pgsql php7-gd && \  
# Install composer  
php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" && \  
php -r "if (hash_file('SHA384', 'composer-setup.php') ===
'669656bab3166a7aff8a7506b8cb2d1c292f042046c5a994c43155c0be6190fa0355160742ab2e1c88d40d5be660b410')
{ echo 'Installer verified'; } else { echo 'Installer corrupt';
unlink('composer-setup.php'); } echo PHP_EOL;" && \  
php composer-setup.php && \  
php -r "unlink('composer-setup.php');" && \  
# Add gosu for easier sudo management  
curl -o /usr/local/bin/gosu -sSL
"https://github.com/tianon/gosu/releases/download/1.2/gosu-amd64" && \  
chmod +x /usr/local/bin/gosu && \  
# Download and extract solder  
wget http://github.com/TechnicPack/TechnicSolder/archive/master.tar.gz -O - |
tar -xzf - -C /var/www && \  
# Better file naming  
mv var/www/TechnicSolder-master var/www/technicsolder && \  
# Install solder dependencies (We have to run it twice, as it sometimes fails
just because)  
cd /var/www/technicsolder && \  
php /composer.phar install --no-dev --no-interaction && \  
php /composer.phar install --no-dev --no-interaction && \  
chown -R nginx . && \  
chmod -R 777 ./app/storage && \  
chmod -R 777 /var/www/technicsolder/public && \  
cd /  
  
# Add gpm for easier file upload  
RUN curl -o /usr/local/bin/gpm -sSL
"https://github.com/zlepper/gpm/releases/download/1.0.1/gpm-1.0.1-linux-x64"
&& \  
chmod +x /usr/local/bin/gpm  
  
# Add gfs for easier file upload  
RUN curl -o /usr/local/bin/gfs -sSL
"https://github.com/zlepper/gfs/releases/download/0.0.4/gfs-linux-x64" && \  
chmod +x /usr/local/bin/gfs  
  
# Allow using an external storage for postgres  
ENV PGDATA=/var/lib/postgresql/data \  
LANG=en_US.utf8\  
# Host used when connection to solder  
SOLDER_HOST=solder.app \  
# Host used when connection to repo  
REPO_HOST=repo.app\  
# Password for postgres  
POSTGRES_PASSWORD=postgres\  
REPO_USER=solder\  
REPO_PASSWORD=solder  
  
# Storage location for postgres data  
VOLUME /var/lib/postgresql/data \  
# Storage location for mod files  
/var/www/repo.solder \  
# Storage location for various special solder files  
/var/www/technicsolder/app/storage \  
# Storage location for another bunch of special solder files  
/var/www/technicsolder/public/storage  
  
  
# Copy setup scripts  
ADD add/ /  
  
RUN chmod +x /var/scripts/setup.sh && \  
chmod +x /var/scripts/setup-postgres.sh  
  
# Make sure the outside can see solder  
EXPOSE \  
# Solder over http  
80 \  
# Solder over https  
443 \  
# Postgres (Mostly available for debugging)  
5432 \  
# GFS  
8080  
# Actually configure solder  
ENTRYPOINT ["/usr/local/bin/gpm"]  
CMD ["-config", "/var/gpm-config.json"]  

