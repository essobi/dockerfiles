FROM that0n3guy/baseimage-nginx-phpfpm:latest  
MAINTAINER Peter Olson <that0n3guy@users.noreply.github.com>  
  
# Install base packages  
ENV DEBIAN_FRONTEND noninteractive  
ENV HOME /root  
  
RUN mv /etc/nginx /etc/nginx.old  
RUN git clone https://github.com/perusio/drupal-with-nginx.git /etc/nginx  
RUN cd /etc/nginx && git checkout D7  
  
# add nginx_ensite for easy use.  
RUN git clone https://github.com/perusio/nginx_ensite.git /root/nginx_ensite  
RUN cp /root/nginx_ensite/nginx_* /usr/sbin  
  
# disable aio per https://github.com/perusio/drupal-with-nginx/issues/136  
RUN sed -i 's/aio on;/#aio on;/g' /etc/nginx/apps/drupal/*.conf  
  
# uncomment unix sockets and comment out phpcgi_tcp  
RUN sed -i 's/#include upstream_phpcgi_unix.conf;/include
upstream_phpcgi_unix.conf;/g' /etc/nginx/nginx.conf  
RUN sed -i 's/include upstream_phpcgi_tcp.conf;/#include
upstream_phpcgi_tcp.conf;/g' /etc/nginx/nginx.conf  
  
# remove backup block and www1 block for unix sockets  
RUN sed -i '/upstream phpcgi_backup/,/}/d'
/etc/nginx/upstream_phpcgi_unix.conf  
RUN sed -i '/upstream www1/,/}/d' /etc/nginx/upstream_phpcgi_unix.conf  
  
# comment out zwei & set to php5  
RUN sed -i 's/server unix:\/var\/run\/php-fpm-zwei.sock;/#server
unix:\/var\/run\/php-fpm-zwei.sock;/g' /etc/nginx/upstream_phpcgi_unix.conf  
RUN sed -i 's/server unix:\/var\/run\/php-fpm.sock;/server
unix:\/var\/run\/php5-fpm.sock;/g' /etc/nginx/upstream_phpcgi_unix.conf  
  
# fix some other error I always get when enabling a site  
RUN sed -i 's/#variables_hash_max_size 1024;/variables_hash_max_size 1024;/g'
/etc/nginx/nginx.conf  
RUN mkdir -p /var/cache/nginx/microcache  
  
# make sure nginx is not a daemon  
RUN echo 'daemon off;' >> /etc/nginx/nginx.conf  
  
EXPOSE 80  
WORKDIR /app  
CMD ["/sbin/my_init"]

