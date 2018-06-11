FROM nginx:alpine  
COPY ./default.conf /etc/nginx/conf.d/  
COPY docker-entrypoint.sh /  
RUN chmod +x /docker-entrypoint.sh  
VOLUME [ "/var/www/html/" ]  
CMD ["/docker-entrypoint.sh"]

