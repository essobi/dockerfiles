FROM alpine:latest  
  
# Labels  
LABEL maintainer="Paulino Padial <github.com/ppadial>"  
  
# Environment variables (with default values)  
ENV LOG_LEVEL=8  
# Configure entrypoint  
ADD docker-entrypoint.sh /docker-entrypoint.sh  
RUN chmod +x /docker-entrypoint.sh  
  
# Volumes declaration  
VOLUME [ "/scripts", "/crontabs" ]  
  
# Start the container process  
ENTRYPOINT ["/docker-entrypoint.sh"]

