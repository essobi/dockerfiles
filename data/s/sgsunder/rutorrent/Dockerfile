FROM php:7-apache  
  
# Install ffmpeg  
RUN apt-get update && \  
apt-get -y install ffmpeg mediainfo git && \  
rm -rf /var/lib/apt/lists/*  
  
# Copy rtorrent from git repository  
RUN git clone \--depth 1 https://github.com/Novik/ruTorrent.git rutorrent && \  
rm -fr rutorrent/.git && \  
# remove config.php and replace it with our own  
rm -f rutorrent/conf/config.php && \  
# remove plugins.ini and replace it with our own  
rm -f rutorrent/conf/plugins.ini  
  
# Copy config.php  
COPY config.php rutorrent/conf/config.php  
# NOTE: use SCGI_PORT SCGI_HOST environment variables  
# Copy plugins.ini  
COPY plugins.ini rutorrent/conf/plugins.ini  
  
# chown/chmod to apache user  
RUN chown -R www-data:www-data rutorrent && \  
chmod -R 755 rutorrent  
  
# TODO copy .htpasswd file or create  
# maybe symlink /etc/apache2/.htpasswd to a docker secret?  
RUN ln -s /run/secrets/auth /etc/apache2/.htpasswd  
  
# Final steps  
EXPOSE 80  

