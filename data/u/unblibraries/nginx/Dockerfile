FROM alpine:latest  
MAINTAINER Jacob Sanford <jsanford_at_unb.ca>  
  
LABEL ca.unb.lib.daemon="nginx"  
LABEL vcs-ref="alpine"  
LABEL vcs-url="https://github.com/unb-libraries/docker-nginx"  
LABEL vendor="University of New Brunswick Libraries"  
  
ENV APP_HOSTNAME nginx.local  
ENV APP_ROOT /app  
ENV NGINX_PID_DIR /run/nginx  
ENV NGINX_PID_FILE $NGINX_PID_DIR/nginx.pid  
ENV NGINX_RUN_GROUP nginx  
ENV NGINX_RUN_USER nginx  
ENV DEPLOY_ENV prod  
  
ENV APP_LOG_DIR $APP_ROOT/log  
ENV APP_WEBROOT $APP_ROOT/html  
  
ENV NGINX_LOG_FILE /proc/self/fd/2  
ENV NGINX_ERROR_LOG_FILE /proc/self/fd/2  
COPY ./conf /conf  
COPY ./scripts /scripts  
  
RUN apk --update add nginx && \  
rm -f /var/cache/apk/* && \  
mkdir -p ${NGINX_PID_DIR} && \  
chown ${NGINX_RUN_GROUP}:${NGINX_RUN_USER} ${NGINX_PID_DIR} && \  
mkdir -p ${APP_WEBROOT} && \  
mkdir -p ${APP_LOG_DIR} && \  
rm /etc/nginx/conf.d/default.conf && \  
cp /conf/nginx/nginx.conf /etc/nginx/nginx.conf && \  
cp /conf/nginx/app.conf /etc/nginx/conf.d/app.conf && \  
chmod -R 755 /scripts  
  
WORKDIR /app  
EXPOSE 80  
ENTRYPOINT ["/scripts/run.sh"]  

