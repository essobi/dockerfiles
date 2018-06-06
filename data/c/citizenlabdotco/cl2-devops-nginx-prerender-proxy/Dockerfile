FROM nginx  
COPY proxy.conf /etc/nginx/proxy.conf  
CMD envsubst '$$WEB_HOST $$PRERENDER_HOST $$PRERENDER_PORT' <
/etc/nginx/proxy.conf > /etc/nginx/conf.d/default.conf && nginx -g 'daemon
off;'  

