FROM tksst/centos:7  
COPY Makefile.patch /tmp/  
COPY build.sh /tmp/  
  
RUN cd /tmp && chmod +x build.sh && ./build.sh  
  
ENTRYPOINT ["stone", "-o", "1005", "-g", "1005", "-t", "/var/empty"]  

