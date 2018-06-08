  
FROM nonameffh/centos:latest  
  
COPY ./registry/registry /bin/registry  
COPY ./registry/config-example.yml /etc/docker/registry/config.yml  
  
VOLUME ["/var/lib/registry"]  
EXPOSE 5000  
COPY docker-entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["/etc/docker/registry/config.yml"]  

