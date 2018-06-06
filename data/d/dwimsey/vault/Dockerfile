#  
FROM vault:0.9.1  
COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh  
RUN mkdir /vault/kubeconfig && chgrp -R 0 /vault && chown -R vault:0 /vault &&
chmod a+x /usr/local/bin/docker-entrypoint.sh  
  

