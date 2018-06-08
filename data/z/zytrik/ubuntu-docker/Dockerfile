FROM ubuntu:trusty  
MAINTAINER Ben Rawson <mail@benrawson.com>  
ADD https://omnitruck.chef.io/install.sh /var/tmp/omnibus-installer.sh  
RUN apt-get update; apt-get install --no-install-recommends -y \  
libwww-perl sudo openssh-server curl lsb-release \  
&& rm -rf /var/lib/apt/lists/*  
RUN ["bash", "/var/tmp/omnibus-installer.sh", "-v", "12.10.24"]  
RUN ["rm", "/var/tmp/omnibus-installer.sh"]  

