FROM debian:jessie  
MAINTAINER Sebastien Astie  
  
# Instructions from: http://www.aptly.info/download/  
RUN echo "deb http://repo.aptly.info/ nightly main" >
/etc/apt/sources.list.d/aptly.list; \  
apt-key adv --keyserver keys.gnupg.net --recv-keys 9E3E53F19C7DE460; \  
apt-get update; \  
apt-get install aptly nano wget xz-utils bzip2 -y  
  
ADD aptly.conf /etc/aptly.conf  
VOLUME ["/aptly"]  
VOLUME ["/etc/apt"]  
VOLUME ["/root"]  
EXPOSE 8080  
CMD ["/usr/bin/aptly", "api", "serve", "-no-lock"]  
  

