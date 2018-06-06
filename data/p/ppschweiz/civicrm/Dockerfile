FROM ppschweiz/wordpress  
  
ENV CIVICRM_VERSION 4.6.16  
RUN apt-get remove -y php5-xcache  
RUN curl -SL
https://download.civicrm.org/civicrm-${CIVICRM_VERSION}-wordpress.zip >
/civicrm-wordpress.zip  
  
COPY docker-entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["apache2", "-DFOREGROUND"]  

