FROM ubuntu:12.04  
MAINTAINER Jonas Bonno Mikkelsen (https://github.com/JonasBonno)  
  
# Installing dependencies  
RUN echo 'deb http://archive.ubuntu.com/ubuntu precise main universe' >
/etc/apt/sources.list  
RUN apt-get update && apt-get install -y \  
nginx && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# nginx not as daemon  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
  
# Expose port 80  
EXPOSE 80  
# Adding file  
ADD default /etc/nginx/sites-available/default  
  
# Start nginx  
CMD ["nginx"]  

