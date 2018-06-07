# Use the omsa image from jose delarosa  
FROM jdelaros1/openmanage  
MAINTAINER Jeff Palmer "https://github.com/palmerit"  
# Log into the container, and download check_openmanage  
RUN wget
http://folk.uio.no/trondham/software/files/check_openmanage-3.7.12.tar.gz && \  
tar -xzvf check_openmanage-3.7.12.tar.gz && \  
mv check_openmanage-3.7.12/check_openmanage /usr/bin/ && \  
chmod +x /usr/bin/check_openmanage && \  
rm -rf check_openmanage-3.7.12  
  

