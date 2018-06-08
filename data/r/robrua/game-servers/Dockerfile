FROM python:slim  
  
  
MAINTAINER Rob Rua <robrua@alumni.cmu.edu>  
  
  
# Add update script  
ADD update.py /root/update.py  
RUN chmod +x /root/update.py  
  
# Add server start script  
ADD start.sh /root/start.sh  
RUN chmod +x /root/start.sh  
  
# Expose factorio port and mount server data volume  
EXPOSE 34197  
VOLUME /root/factorio  
  
# Ready  
WORKDIR /root/factorio  
CMD /root/update.py && /root/start.sh

