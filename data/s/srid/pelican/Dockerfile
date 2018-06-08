FROM srid/dropbox  
  
RUN apt-get -qy install python-pelican nginx-light  
  
ADD start /image/hooks/  
  
ENV PELICAN_DIR ${DROPBOX_DIR}/Pelican  
ENV DROPBOX_WATCH_DIR ${PELICAN_DIR}  
ENV DROPBOX_POST_UPDATE_COMMAND make html

