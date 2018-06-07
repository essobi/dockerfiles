FROM debian:jessie  
  
# Docker will run as root while building the image (technically this is the  
# default behavior, specifying here for clarity). This is also the user that  
# OrientDB will run as.  
USER root  
  
# Add provisioning script  
ADD docker-*.sh /tmp/docker/  
  
# provision the image  
RUN sh /tmp/docker/docker-provision.sh  
  
WORKDIR /opt/orientdb/  
EXPOSE 2424  
EXPOSE 2480  
ENTRYPOINT ["/entrypoint.sh"]  
  
# Start OrientDB when the container starts by default  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]  

