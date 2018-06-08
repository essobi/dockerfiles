FROM rancher/vm-base:0.0.3  
MAINTAINER obed.n.munoz@gmail.com  
  
RUN apt-get update  
RUN apt-get install xz-utils  
  
COPY clearlinux.sh /usr/bin/  
RUN /usr/bin/clearlinux.sh  
  
CMD ["-m 512m"]  

