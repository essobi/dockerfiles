#This will prepare a elasticsearch node with mongo-connector enabled  
FROM mongo:3.0  
MAINTAINER yeasy@github  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV TZ Asia/Shanghai  
  
COPY docker-entrypoint.sh /tmp/  
  
# Sample usage when no commands is given outside  
ENTRYPOINT ["/bin/bash", "/tmp/docker-entrypoint.sh"]  

