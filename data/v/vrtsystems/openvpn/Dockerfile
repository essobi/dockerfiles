# Pull in base image  
FROM vrtsystems/baseimage  
MAINTAINER VRT Engineering <engineering@vrt.com.au>  
  
# Update repostory cache and install dependencies for VPN server  
RUN apt-get update && apt-get -y install openvpn  
  
# Expose ports for OpenVPN  
EXPOSE 1194/udp  
  
# Copy supervisord configuration for OpenVPN  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
# Command to run when starting the container  
CMD ["supervisord"]  

