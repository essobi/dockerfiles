FROM lesaux/diamond-containercollector  
COPY diamond/diamond.conf /etc/diamond/diamond.conf  
COPY diamond/collectors/DockerContainerCollector.conf
/etc/diamond/collectors/DockerContainerCollector.conf  
COPY entrypointWrapper.sh /  
COPY dockercontainer.py /usr/local/share/diamond/collectors/dockercontainer/  
RUN chmod +x /entrypointWrapper.sh  
  
# Default prefix value  
ENV PREFIX coco.servers  
  
# remove the entry point and add a cmd  
ENTRYPOINT []  
CMD ["/entrypointWrapper.sh"]

