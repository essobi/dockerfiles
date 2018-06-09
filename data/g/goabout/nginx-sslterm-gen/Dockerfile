FROM goabout/alpine  
  
MAINTAINER Go About <tech@goabout.com>  
  
ENV DOCKER_HOST unix:///tmp/docker.sock  
  
COPY docker-gen /usr/local/bin/docker-gen  
RUN chmod +x /usr/local/bin/docker-gen  
  
COPY docker-gen.cfg /templates/etc/docker-gen.cfg  
COPY nginx.conf.tmpl /templates/etc/nginx/conf.d/sslterm.conf.tmpl  
COPY ssl_certificate.pem /templates/etc/nginx/conf.d/ssl_certificate.pem  
COPY ssl_certificate_key.pem
/templates/etc/nginx/conf.d/ssl_certificate_key.pem  
  
VOLUME ["/etc/nginx/conf.d"]  
  
ENTRYPOINT ["entrypoint", "--"]  
CMD ["docker-gen", "-config", "/etc/docker-gen.cfg"]  

