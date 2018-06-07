#  
# Traefik Proxy Docker Image  
#  
# Repository: https://github.com/Salalem/traefik-proxy  
# Maintainers:  
# \- George Khoury <george@salalem.com>  
  
# Use 'traefik:v1.6.0' as a base image.  
FROM traefik:v1.6.0  
  
# Expose necessary ports for traefik to bind to host.  
EXPOSE 80 443  
  
# Copy modified configuration file into '/etc/traefik'  
COPY ./traefik /etc/traefik  

