FROM nginx:1.11.10-alpine  
LABEL org.label-schema.name='nginx'  
RUN apk update && apk add sed && rm -rf /var/cache/apk  
COPY ./nginx.conf /etc/nginx/conf.d/default.conf  
CMD sed "s|{{SPIRAL_COREAI_HOSTNAME}}|${SPIRAL_COREAI_HOSTNAME}|g" -i
/etc/nginx/conf.d/default.conf && \  
nginx -g 'daemon off;'  

