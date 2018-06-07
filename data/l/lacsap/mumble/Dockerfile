############################################################  
# Dockerfile to build a mumble server that works with supervisor  
############################################################  
  
FROM debian:8  
  
# Install Requirements  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y \  
mumble-server \  
supervisor \  
pwgen  
  
# load configs in the image  
COPY etc/supervisor/supervisord.conf /etc/supervisor/supervisord.conf  
COPY etc/supervisor/conf.d/murmurd.conf /etc/supervisor/conf.d/murmurd.conf  
COPY etc/mumble-server.ini /etc/mumble-server.ini  
COPY server_start /server_start  
  
# Make server_start executable  
RUN chmod +x /server_start  
  
EXPOSE 64738  
VOLUME ["/data"]  
CMD ["/server_start"]  

