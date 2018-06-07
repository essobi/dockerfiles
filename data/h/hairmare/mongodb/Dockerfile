FROM hairmare/gentoo  
MAINTAINER Lucas Bickel <hairmare@purplehaze.ch>  
  
# configure install  
ENV GENTOO_WORLD_PACKAGES dev-db/mongodb  
  
# install mongodb  
RUN emerge $GENTOO_WORLD_PACKAGES -q  
  
# configure package  
RUN chown mongodb:mongodb /var/lib/mongodb  
  
# configure runtime  
VOLUME /var/lib/mongodb  
  
USER mongodb  
  
ENTRYPOINT [ \  
"mongod", \  
"--port", "27017", \  
"--dbpath", "/var/lib/mongodb", \  
"--unixSocketPrefix", "/tmp" \  
]  
#CMD [ "--journal" ]  
EXPOSE 27017 28017  

