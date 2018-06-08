FROM node:4.4.7-slim  
MAINTAINER Valudio <development@valudio.com>  
  
# Locale issue  
ENV LC_ALL="POSIX" \  
METEOR_VERSION=latest  
  
COPY start.sh start.sh  
RUN sh start.sh && rm start.sh  
  
# VOLUME /app  
WORKDIR /app  
EXPOSE 3000  
CMD ["bash"]  
  

