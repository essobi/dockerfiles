FROM lastnico/nominatim  
MAINTAINER Max Bohnet <bohnet@ggr-planung.de>  
  
ARG NOMINATIM_HOME=/app  
COPY local.php ${NOMINATIM_HOME}/build/settings/local.php  
  
VOLUME /importdata  
  
CMD /app/entrypoint.sh  

