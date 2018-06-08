FROM nginx  
  
# Change pid file location  
# Remove nginx user  
# Change port to 8080  
# modify perms for non-root runtime  
  
RUN sed -i 's/\/var\/run\/nginx.pid/\/var\/cache\/nginx\/nginx.pid/g'
/etc/nginx/nginx.conf \  
&& sed -i -e '/user/!b' -e '/nginx/!b' -e '/nginx/d' /etc/nginx/nginx.conf \  
&& sed -i -e '/listen/!b' -e '/80;/!b' -e 's/80;/8080;/'
/etc/nginx/conf.d/default.conf \  
&& chown -R 998 /var/cache/nginx /etc/nginx /usr/share/nginx/html \  
&& chmod -R g=u /var/cache/nginx /etc/nginx /usr/share/nginx/html  
  
VOLUME ["/var/cache/nginx"]  
  
EXPOSE 8080 8443  
  
USER 998  

