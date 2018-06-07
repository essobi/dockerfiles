FROM ubuntu:trusty  
MAINTAINER Olof Nilsson <olof@drp.nu>  
  
# Workaround to get rid of ugly red text when building from Dockerfile  
ENV DEBIAN_FRONTEND "noninteractive"  
# Install Nginx  
RUN apt-get install -qy software-properties-common && \  
add-apt-repository -y ppa:nginx/stable && \  
apt-get update -q && \  
apt-get install -qy \  
nginx && \  
rm -rf /var/lib/apt/lists/* && \  
echo "\ndaemon off;" >> /etc/nginx/nginx.conf  
  
# Expose Volumes  
VOLUME ["/etc/nginx", \  
"/var/log/nginx", \  
"/var/www/html"]  
  
# Expose Port - HTTP  
EXPOSE 80  
# Expose Port - HTTPS  
EXPOSE 443  
# Define Working Directory  
WORKDIR /etc/nginx  
  
# Define Default Command  
CMD ["nginx"]  
  

