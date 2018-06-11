FROM virtuman/nginx-php-exim-memcached:latest  
  
MAINTAINER Alexei Smirnov <alexei@virtuman.com>  
  
RUN rm -f /etc/service/sshd/down  
  
# Regenerate SSH host keys. baseimage-docker does not contain any, so you  
# have to do that yourself. You may also comment out this instruction; the  
# init system will auto-generate one during boot.  
RUN /etc/my_init.d/00_regen_ssh_host_keys.sh  
  
RUN curl -o /usr/local/bin/wp-cli.phar https://raw.githubusercontent.com/wp-
cli/builds/gh-pages/phar/wp-cli.phar && \  
chmod +x /usr/local/bin/wp-cli.phar && \  
echo 'alias wp="/sbin/setuser ${APP_USER:-$DEFAULT_APP_USER}
/usr/local/bin/wp-cli.phar"' >> /root/.bashrc && \  
rm -rf /etc/nginx/sites-enabled/default-ssl.conf  
  
WORKDIR /var/www  

