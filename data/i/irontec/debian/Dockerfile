FROM php:7.0.11-apache  
  
#install tini  
ENV TINI_VERSION v0.10.0  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
/tini  
RUN chmod +x /tini  
  
ENTRYPOINT ["/tini", "--"]  
  
CMD ["apache2-foreground"]

