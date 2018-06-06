FROM nginx:latest  
  
MAINTAINER "Lisa Ridley <lisa@prometsource.com>"  
#COPY nginx.conf /etc/nginx/nginx.conf  
COPY default.conf /etc/nginx/conf.d/default.conf  
  
RUN touch /var/run/nginx.pid \  
&& chown -Rf www-data:www-data /var/run/nginx.pid \  
&& chown -Rf www-data:www-data /var/cache/nginx \  
&& chown -Rf www-data:www-data /etc/nginx  
  
EXPOSE 8080 8443  
USER www-data  
  
VOLUME /var/www/html  
  
CMD ["nginx", "-g", "daemon off;"]

