# Liferay Data Container  
#  
# VERSION 0.0.1  
#  
# 0.0.1 : initial creation of image for the liferay data container with config
for postgres  
FROM debian:jessie  
  
MAINTAINER Robert Reihs <robert.reihs@gmail.com>  
  
ADD init-config.sh /usr/local/bin/init-config.sh  
  
# Keep container from shutting down until explicitly stopped  
ENTRYPOINT ["/bin/sh"]  
CMD ["/usr/local/bin/init-config.sh"]

