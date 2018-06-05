FROM uazlibraries/debian-php-fpm:latest  
  
ENV FILESENDER_V=2.0-rc1 SSP_V=1.15.0  
RUN \  
cd /opt && \  
curl -kL
https://github.com/filesender/filesender/archive/filesender-$FILESENDER_V.tar.gz
| tar xz && \  
mv filesender-filesender-$FILESENDER_V filesender && \  
curl -L
https://github.com/simplesamlphp/simplesamlphp/releases/download/v${SSP_V}/simplesamlphp-${SSP_V}.tar.gz
| tar xz && \  
mv simplesamlphp-${SSP_V} simplesamlphp  
  
# Add filesender and simplesamlphp configuration to /opt/conf  
ADD template /opt/template  
  
# Ensure correct runtime permissions - php-fpm runs as www-data  
RUN chown -R www-data.www-data /opt/*  
  
# Add setup and startup config files to /  
ADD docker/* /  
  
VOLUME ["/opt/filesender", "/opt/simplesamlphp"]  
  
CMD ["/entrypoint.sh"]  

