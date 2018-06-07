FROM inodes/docker-x86-rtlsdr-baseimage:latest  
  
MAINTAINER Glenn Stewart <docker@inodes.net>  
  
# Uses Ted Luis Mutability dump1090  
# See:  
# https://github.com/tedsluis/dump1090.git  
WORKDIR /tmp  
  
RUN git clone https://github.com/tedsluis/dump1090.git \  
&& cd /tmp/dump1090 \  
&& make  
  
WORKDIR /tmp/dump1090  
  
EXPOSE 8080 30001 30002 30003 30004 30005  
ENTRYPOINT ["./dump1090"]  

