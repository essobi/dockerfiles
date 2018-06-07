FROM openresty/openresty:centos  
  
COPY ./docker_entrypoint.sh /usr/local/bin/docker_entrypoint.sh  
  
COPY ./nginx.conf /etc/nginx/conf.d/cube.conf  
  
RUN chmod 777 /usr/local/bin/docker_entrypoint.sh  
  
ENTRYPOINT ["/usr/local/bin/docker_entrypoint.sh"]

