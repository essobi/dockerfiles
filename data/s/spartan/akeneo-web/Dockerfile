FROM nginx  
  
EXPOSE 80  
ENV APP_ENVIRONMENT='production' \  
WEB_PHP_HOST='php' \  
WEB_SERVER_NAME='akeneo.local' \  
WEB_ERROR_LOG_LEVEL='warn' \  
WEB_STATUS_ALLOWED_IP='127.0.0.1' \  
WEB_CLIENT_MAX_BODY_SIZE='2m'  
ENTRYPOINT ["/usr/local/bin/entrypoint"]  
  
CMD ["nginx"]  
  
COPY entrypoint* /usr/local/bin/  
  
COPY nginx.conf /etc/nginx/nginx.conf  
  
COPY akeneo.conf /etc/nginx/conf.d/akeneo.template  
  
RUN rm /etc/nginx/conf.d/default.conf  
  
RUN apt-get update && \  
apt-get install -y gettext-base  

