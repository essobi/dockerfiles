FROM nginx:latest  
  
# setup environment  
ENV LATEST_RELEASE=0.2.2-alpha  
ENV CONFIG_FILE=  
ENV NGINX_CONFIG_FILE=/etc/nginx/conf.d/default.conf  
ENV EXTRA_ARGS=  
  
# download binary & default template  
ADD
https://raw.githubusercontent.com/honsiorovskyi/nginx_config_updater/$LATEST_RELEASE/default.conf.tmpl
\  
/opt/nginx_config_updater/default.conf.tmpl  
ADD
https://github.com/honsiorovskyi/nginx_config_updater/releases/download/$LATEST_RELEASE/nginx_config_updater
\  
/opt/nginx_config_updater/bin/nginx_config_updater  
RUN chmod +x /opt/nginx_config_updater/bin/nginx_config_updater  
  
# expose port  
EXPOSE 3456  
# run updater & nginx  
CMD ( sleep 0.5 && /opt/nginx_config_updater/bin/nginx_config_updater \  
\--config=${CONFIG_FILE} \  
\--template=/opt/nginx_config_updater/default.conf.tmpl \  
\--out=${NGINX_CONFIG_FILE} \  
\--listen=:3456 \  
${EXTRA_ARGS} ) \  
& nginx -g "daemon off;"  

