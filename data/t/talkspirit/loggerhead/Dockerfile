FROM ubuntu:16.04  
  
# Environments  
ENV BZR_SERVED_BRANCHES /srv/bzr  
ENV BZR_PREFIX /loggerhead/  
  
RUN apt-get update && apt-get upgrade -y  
  
RUN apt-get install loggerhead sudo -y  
RUN ln -s /usr/share/loggerhead/static /usr/lib/python2.7/dist-
packages/loggerhead/static  
  
COPY entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["sh", "/entrypoint.sh"]  

