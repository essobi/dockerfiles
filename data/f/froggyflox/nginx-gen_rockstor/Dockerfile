FROM jwilder/docker-gen  
  
COPY default.cfg /etc/docker-gen/templates/default.cfg  
  
# CMD ["-watch", "-wait 5s:30s", "-notify-sighup nginx", "/etc/docker-
gen/templates/nginx.tmpl", "/etc/nginx/conf.d/default.conf"]  
CMD ["-config", "/etc/docker-gen/templates/default.cfg"]  

