FROM ubuntu:artful  
  
MAINTAINER Josh Bohde <josh.bohde@reconfigure.io>  
  
RUN apt-get update && apt-get install -y \  
verilator \  
libfindbin-libs-perl  
  
WORKDIR /mnt  
ENTRYPOINT ["verilator"]

