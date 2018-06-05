FROM ubuntu:xenial  
MAINTAINER atomney <atomney+docker@gmail.com>  
  
# If you want a volume to keep updates in, uncomment the following line.  
#VOLUME ["/var/cache/apt-cacher-ng"]  
# Update and install  
RUN apt-get update && apt-get install -y apt-cacher-ng nano vim curl && \  
curl https://www.centos.org/download/full-mirrorlist.csv | sed
's/^.*"http:/http:/' | sed 's/".*$//' | grep ^http >/etc/apt-cacher-
ng/centos_mirrors && \  
rm /etc/apt-cacher-ng/acng.conf  
  
# Copy custom config into container  
COPY acng.conf /etc/apt-cacher-ng/acng.conf  
  
# Expose the apt-cacher-ng port  
EXPOSE 3142  
# Run apt-cacher-ng on container start.  
CMD chmod 777 /var/cache/apt-cacher-ng && /etc/init.d/apt-cacher-ng start &&
tail -f /var/log/apt-cacher-ng/*  
  

