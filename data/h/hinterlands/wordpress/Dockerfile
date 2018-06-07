FROM hinterlands/php7-nginx-alpine  
LABEL maintainer "Andrew Li <andrew.li@hinterlands.tech>"  
  
ENV TERM="xterm" \  
DB_HOST="172.17.0.1" \  
DB_NAME="" \  
DB_USER="" \  
DB_PASS="" \  
WP_VERSION="" \  
WP_LOCALE=""  
RUN curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-
cli.phar && chmod +x wp-cli.phar && php wp-cli.phar --info && mv wp-cli.phar
/bin/wp-cli && chown nginx:nginx /bin/wp-cli  
  
ADD files/default.conf /etc/nginx/conf.d/  
ADD files/run-pre.sh /  
RUN chmod +x /run-pre.sh  
  
EXPOSE 80  
VOLUME ["/usr"]  
  
CMD ["/run.sh"]  

