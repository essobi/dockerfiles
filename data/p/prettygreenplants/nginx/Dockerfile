# Pull base image  
FROM nginx:alpine  
  
MAINTAINER Pretty Green Plants <info@prettygreenplants.com>  
  
ENV NGINX_HOST local.prettygreenplants  
ENV USE_SELF_SIGNED_CERTIFICATE true  
  
# Install usermod command for alpine - should be included by default from
alpine  
RUN echo http://dl-2.alpinelinux.org/alpine/edge/community/ >>
/etc/apk/repositories  
RUN apk --no-cache add shadow tzdata  
  
# Set timezone  
ENV TZ=Asia/Phnom_Penh  
RUN ln -nfs /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone  
  
# Create webserver user and group  
RUN addgroup -g 1000 -S prettygreenplants  
RUN adduser -G prettygreenplants -S -D -H -u 1000 prettygreenplants  
  
# Copy configuration files for nginx  
COPY nginx.conf /etc/nginx/nginx.conf  
COPY nginx_vhost.conf /etc/nginx/conf.d/default.conf  
COPY ssl/self-signed.cert /etc/ssl/certs/prettygreenplants-self-signed.cert  
COPY ssl/self-signed.key /etc/ssl/private/prettygreenplants-self-signed.key  
  
RUN sed -i -e "s~###DEFAULT_NGINX_HOST###~${NGINX_HOST}~g"
/etc/nginx/conf.d/default.conf  
  
# Set entrypoint to fix volume mount permission  
COPY entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
WORKDIR /etc/nginx/conf.d  
  
EXPOSE 80 443  
CMD ["nginx", "-g", "daemon off;"]  

