#  
# Author: Rohith  
# Date: 2015-07-20 16:46:09 +0100 (Mon, 20 Jul 2015)  
#  
# vim:ts=2:sw=2:et  
#  
FROM prom/prometheus:latest  
MAINTAINER Rohith <gambol99@gmail.com>  
  
ADD config/prometheus.yml /etc/prometheus/prometheus.yml  
  
RUN mkdir -p /etc/prometheus/targets.d  
  
ENTRYPOINT [ "/bin/prometheus" ]  
CMD [ "-config.file=/etc/prometheus/prometheus.yml", \  
"-storage.local.path=/prometheus", \  
"-web.console.libraries=/etc/prometheus/console_libraries", \  
"-web.console.templates=/etc/prometheus/consoles", \  
"-web.listen-address=:9090" ]  

