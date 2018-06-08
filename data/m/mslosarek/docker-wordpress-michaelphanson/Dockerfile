FROM wordpress  
MAINTAINER Mark Slosarek  
  
COPY ./src/arjuna-x /usr/src/wordpress/wp-content/themes/arjuna-x  
  
COPY ./src/akismet /usr/src/wordpress/wp-content/plugins/akismet  
COPY ./src/amazon-s3-and-cloudfront /usr/src/wordpress/wp-
content/plugins/amazon-s3-and-cloudfront  
COPY ./src/amazon-web-services /usr/src/wordpress/wp-content/plugins/amazon-
web-services  
COPY ./src/google-sitemap-generator /usr/src/wordpress/wp-
content/plugins/google-sitemap-generator  
COPY ./src/relative-url /usr/src/wordpress/wp-content/plugins/relative-url  
COPY ./src/wp-mail-smtp /usr/src/wordpress/wp-content/plugins/wp-mail-smtp  
COPY ./src/xcloner-backup-and-restore /usr/src/wordpress/wp-
content/plugins/xcloner-backup-and-restore  
  
  
EXPOSE 80  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["apache2", "-DFOREGROUND"]

