##################################################################  
## ##  
## Docker file of Docker image with MySQL for WARP projects ##  
## ##  
##################################################################  
## Table of contents  
##  
## 1. Base image and developers  
## 2. Install packages  
## 3. Set default cmd  
## 4. Set entrypoint  
##  
  
# 1. Base image and developers  
FROM mysql:5.7  
MAINTAINER German Manvelov <gtmmm2011@gmail.com>  
  
# 2. Installation of packages  
RUN apt-get update && apt-get install -y \  
  
supervisor \  
; exit 0  
  
# 3. Set default cmd  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor.d/supervisor-docker-mysql-
dev.ini"]  
  
# 4. Set entrypoint  
# ENTRYPOINT ["docker-entrypoint.sh"]  

