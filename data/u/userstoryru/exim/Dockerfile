FROM ubuntu:16.04  
# update  
RUN apt-get update  
  
# update  
RUN apt-get install -y exim4-daemon-heavy  
  
EXPOSE 25  
#CMD ["exim", "-bd", "-v", "-q30m"]  
COPY start.sh /usr/bin/  
  
CMD ["start.sh"]  

