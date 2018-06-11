FROM ulock/postgres-wale  
  
# Image settings  
MAINTAINER Xavier Jodoin <xavier@jodoin.me>  
CMD /opt/app/bin/boot  
  
# Make symlinks for the wrapper  
RUN ln -s /opt/app/bin/wal-e-wrapper /usr/local/bin/wal-e-wrapper  
  
# Install core app files  
ADD app /opt/app  

