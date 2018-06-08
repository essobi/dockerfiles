FROM debian:8.5  
  
ENV TERM=xterm  
  
RUN apt-get update && \  
# Install dependencies  
apt-get install -y --no-install-recommends \  
curl \  
imagemagick \  
ghostscript \  
php5 \  
php5-cli \  
php5-curl \  
php5-fpm \  
php5-imagick \  
php5-mcrypt \  
php5-mysqlnd \  
nano \  
ca-certificates \  
sudo \  
unzip \  
&& \  
# Install Composer  
curl -ksS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer && \  
  
# Create props user  
adduser --disabled-password --gecos '' props && \  
adduser props sudo && \  
echo 'props ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers && \  
su - props -c 'touch /home/props/.sudo_as_admin_successful' && \  
  
# Create application directory and give props user ownership of it  
mkdir /var/props && \  
chown -R props:props /var/props && \  
  
# Cleanup  
rm -r /var/lib/apt/lists/*  
  
# Copy in PHP-FPM config  
COPY php-fpm.conf /etc/php5/fpm/php-fpm.conf  
  
# Set default user to props  
USER props  
  
# Expose PHP-FPM port  
EXPOSE 9000  
  
# Run PHP-FPM  
CMD sudo php5-fpm  

