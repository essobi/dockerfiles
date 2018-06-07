FROM kricker/prod-server-base:latest  
  
ENV REBUILD yes  
  
# Install Composer.  
RUN curl -sS https://getcomposer.org/installer | php  
RUN mv composer.phar /usr/local/bin/composer  
  
# Install Drush 7.  
RUN composer global require drush/drush:7.*  
RUN composer global update  
RUN ln -s /root/.composer/vendor/bin/drush /usr/bin  
  
# download drush recipes  
RUN drush dl drush_recipes-7.x-1.x-dev -y  
  
# For compatibility with Kalabox 2  
# The data container will manage these config files if using kalabox.  
# Because we are awesome, we will not force these settings should some wish
not to use kalabox.  
# for f in /src/config/* /src/config/**/* ; do  
# ns=${f/\/src/config/}  
# if [ -f "$ns" ] || [ -h "$ns" ];  
# then  
# rm "$ns" && ln -s "/src/config{$f}" "$ns";  
# done;  
# Create a src directory for voluming with project root if it doesn't exist.  
RUN if [ ! -d /src ]; then mkdir /src; fi  
  
# Create symbolic links for php config files  
COPY config /root/config  
RUN rsync -a /root/config/ /src/config && rm -rf /root/config  
RUN chmod -R 777 /src  
RUN sh /src/config/php-symlinks.sh  
  
# Create symbolic links for nginx config files  
RUN sh /src/config/nginx-symlinks.sh  
  
# Create symbolic links for apache config files  
RUN sh /src/config/apache-symlinks.sh  
  
# Add .htaccess file to site root  
ADD .htaccess /root/.htaccess  
  
# Set the symbolic link from /data to siteroot  
RUN mda=/srv/www/siteroot; if ! [ -L $mda ]; then ln -s /data
/srv/www/siteroot; fi  
  
# Add start script.  
RUN chmod -R 777 /src/config  
  
# Define default command.  
CMD sh /root/server-base-start.sh && \  
sh /root/prod-server-base-start.sh && \  
sh /root/varnish-start.sh & \  
/bin/bash /src/config/drupal-base-start.sh && \  
/sbin/my_init  

