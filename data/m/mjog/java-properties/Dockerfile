#  
# java Dockerfile  
#  
# https://bitbucket.org/mjogltd/java-properties  
#  
# Pull the official java base image  
FROM java:openjdk-8-jre  
  
# Entrypoint script  
COPY docker-entrypoint.sh /entrypoint.sh  
COPY env.awk /env.awk  
RUN chmod +x /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  

