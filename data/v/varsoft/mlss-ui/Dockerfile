FROM nginx:1.10.1-alpine  
  
EXPOSE 80  
RUN rm -v /etc/nginx/conf.d/*.conf  
ADD settings.js.template /settings.js.template  
ADD nginx.conf.template /nginx.conf.template  
  
ADD application /www  
WORKDIR /www  
  
CMD envsubst '\$UI_SENDFILE \$FOLDER \$VIRTUAL_HOST' < /nginx.conf.template >
/etc/nginx/conf.d/default.conf \  
&& envsubst < /settings.js.template > /www/dev/assets/js/settings.js \  
&& envsubst < /settings.js.template > /www/production/assets/js/settings.js \  
&& nginx -g 'daemon off;';

