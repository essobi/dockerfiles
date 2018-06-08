FROM wordpress:php7.1  
LABEL mantainer="Giuseppe Iannelli <https://github.com/giuseppeiannelli>"  
  
ENV ENABLE_XMLRPC false  
  
COPY docker-entrypoint.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/docker-entrypoint.sh  
  
ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]  
CMD ["apache2-foreground"]

