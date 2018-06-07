FROM docker:1.12.2-rc3  
MAINTAINER kappabull <kappa8v11@gmail.com>  
  
EXPOSE 2377/tcp 7946 4789  
ENV MANAGER_ADDRESS \  
MANAGER_PORT \  
TOKEN  
  
ADD entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
ENTRYPOINT ["/bin/sh", "/entrypoint.sh"]

