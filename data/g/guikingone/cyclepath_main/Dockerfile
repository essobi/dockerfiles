FROM gcr.io/google_appengine/php  
  
ARG app_env  
ARG app_debug  
ARG app_secret  
  
ENV DOCUMENT_ROOT=${APP_DIR}/public \  
APP_ENV=$app_env \  
APP_DEBUG=$app_debug \  
APP_SECRET=$app_secret \  
PHP_INI_OVERRIDE=docker/php/conf/production/php.ini  
  
RUN cp -R ${APP_DIR} ${APP_DIR}-copy; rm -r ${APP_DIR}; mv ${APP_DIR}-copy
${APP_DIR}; chmod -R 550 ${APP_DIR}; chown -R root.www-data ${APP_DIR}  

