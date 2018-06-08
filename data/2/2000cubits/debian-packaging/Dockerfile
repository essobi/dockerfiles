FROM 2000cubits/base:latest  
MAINTAINER Michal Moravec "michi.m@gmail.com"  
  
RUN apt-get update && \  
apt-get -y --no-install-recommends install git ssh-client dh-make build-
essential autoconf autotools-dev devscripts fakeroot && \  
apt-get -y -u dist-upgrade && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
CMD ["/usr/local/bin/boot-debian-base"]  

