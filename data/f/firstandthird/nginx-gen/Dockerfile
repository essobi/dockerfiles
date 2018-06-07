FROM jwilder/docker-gen:0.7.3  
ADD nginx.tmpl /etc/docker-gen/templates/nginx.tmpl  
  
VOLUME /etc/nginx/certs  
  
#RUN sed -i -e"s/access.log vhost/access.log json/" /etc/docker-
gen/templates/nginx.tmpl  
CMD [ "-notify-sighup", "nginx", "-watch", "/etc/docker-
gen/templates/nginx.tmpl", "/etc/nginx/conf.d/default.conf" ]  

