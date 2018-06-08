FROM opsbears/mariadb:stable  
  
RUN sed -i -e 's/#!\/bin\/sh/#!\/bin\/bash/' /usr/bin/wsrep_sst_rsync  
COPY init.sh /init.sh  

