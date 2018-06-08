############################################################  
# Dockerfile to build Genropy container images  
# Based on Ubuntu  
############################################################  
  
FROM genropy/genropy  
MAINTAINER Francesco Porcari - francesco@genropy.org  
  
ADD . /home/genropy_projects/sandbox  
EXPOSE 8080  
  
ENV GNR_CURRENT_SITE sandbox  
ENV GNR_WSGI_OPT_remote_edit t  
  
  
ENTRYPOINT ["/usr/bin/supervisord"]  
  

