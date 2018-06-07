FROM jwilder/docker-gen:0.7.3  
ENV UPDATER_CONTAINER=hosts-updater  
  
COPY hosts.tmpl /etc/docker-gen/templates/hosts.tmpl  
  
ENTRYPOINT []  
  
CMD ["/bin/sh", "-c", "/usr/local/bin/docker-gen -notify-sighup
${UPDATER_CONTAINER} -watch /etc/docker-gen/templates/hosts.tmpl /hosts/gen"]

