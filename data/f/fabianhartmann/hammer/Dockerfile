FROM python:3  
MAINTAINER fabian.hartmann@bluewin.ch  
  
# Enviroment Variables for Datacontainer and Restore from Backup.  
ENV DEST_HOST=127.0.0.1  
# adds my scrippt with some functions.  
ADD ./hammermanager.sh /srv/hammermanager.sh  
ADD ./hammer-master/* /srv/hammer-master/  
  
CMD /bin/bash -C /srv/hammermanager.sh

