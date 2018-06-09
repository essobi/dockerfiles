############################################################  
# Dockerfile to run superbeer/api Containers  
#  
############################################################  
  
FROM django:python2-onbuild  
MAINTAINER Lola Rigaut-Luczak <rllola80@gmail.com>  
  
# Important Mise à jour toujours avant  
RUN apt-get -y update  
  
# To teddy a bit the room  
RUN apt-get -y autoremove  
  
# Geo spatials c++ librairies  
RUN apt-get install -y binutils libproj-dev gdal-bin  
  
RUN useradd -u 1000 -g 100 -d /home/django django  
  
USER django  
  
ADD ./scripts/docker-entrypoint.sh /home/django/  
  
ENTRYPOINT ["/bin/bash", "-e", "/home/django/docker-entrypoint.sh"]  
  
  

