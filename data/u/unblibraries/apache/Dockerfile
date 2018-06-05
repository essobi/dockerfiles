FROM alpine:3.4  
MAINTAINER Jacob Sanford <jsanford_at_unb.ca>  
  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_RUN_USER apache  
ENV APP_HOSTNAME apache.local  
ENV APP_ROOT /app  
ENV DEPLOY_ENV prod  
  
ENV APP_LOG_DIR $APP_ROOT/log  
ENV APP_WEBROOT $APP_ROOT/html  
  
ENV APACHE_LOG_FILE /proc/self/fd/2  
ENV APACHE_ERROR_LOG_FILE /proc/self/fd/2  
RUN apk --update add apache2 && \  
mkdir -p /run/apache2 && \  
rm -f /var/cache/apk/* && \  
mkdir -p ${APP_WEBROOT} && \  
mkdir -p ${APP_LOG_DIR}  
  
COPY conf/apache2/app.conf /etc/apache2/conf.d/app.conf  
  
COPY scripts /scripts  
RUN chmod -R 755 /scripts  
  
WORKDIR /app  
EXPOSE 80  
ENTRYPOINT ["/scripts/run.sh"]  

