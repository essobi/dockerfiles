# Drone.io docker image  
#  
# # Usage  
# mkdir -p /etc/docker/drone  
# docker run --rm --name drone -p 80:80 -v /etc/docker/drone/:/var/lib/drone/
zedtux/drone  
# open http://<ip-address>/install  
#  
FROM debian:jessie  
MAINTAINER Guillaume Hain zedtux@zedroot.org  
  
RUN apt-get update && \  
apt-get install -y wget mailutils && \  
wget http://downloads.drone.io/latest/drone.deb && \  
dpkg -i drone.deb  
  
ADD drone_start /usr/local/bin/  
RUN chmod +x /usr/local/bin/drone_start  
  
VOLUME ["/var/lib/drone/"]  
VOLUME ["/var/log/upstart/"]  
  
EXPOSE 25  
EXPOSE 80  
ENTRYPOINT ["drone_start"]  

