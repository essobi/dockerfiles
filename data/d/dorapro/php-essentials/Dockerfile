FROM dorapro/composer  
  
ENV CS_FIXER_VERSION v1.12.0  
ENV CODE_SNIFFER_VERSION 2.5.1  
ENV MESS_DETECTOR_VERSION 2.4.3  
ENV METRICS_VERSION v1.10.0  
ENV LOC_VERSION 3.0.1  
RUN composer global require --no-scripts --prefer-dist --update-no-dev \  
friendsofphp/php-cs-fixer:${CS_FIXER_VERSION} \  
squizlabs/php_codesniffer:${CODE_SNIFFER_VERSION} \  
phpmd/phpmd:${MESS_DETECTOR_VERSION} \  
phpmetrics/phpmetrics:${METRICS_VERSION} \  
phploc/phploc:${LOC_VERSION} \  
&& composer clear-cache  
  
CMD []  
ENTRYPOINT []  

