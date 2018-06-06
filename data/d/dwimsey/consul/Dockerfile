#  
FROM consul:latest  
  
# Install or update needed tools.  
COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh  
  
RUN mkdir /consul/kubeconfig && chgrp -R 0 /consul && chown -R consul:0
/consul && chmod a+x /usr/local/bin/docker-entrypoint.sh && chmod g+w
/etc/passwd  
  
ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]  
  
# By default you'll get an insecure single-node development server that stores  
# everything in RAM, exposes a web UI and HTTP endpoints, and bootstraps
itself.  
# Don't use this configuration for production.  
CMD ["agent", "-dev", "-client", "0.0.0.0"]  

