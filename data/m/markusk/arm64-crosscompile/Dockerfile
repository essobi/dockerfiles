FROM debian:stretch  
MAINTAINER Markus Kasten <github@markuskasten.eu>  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y build-essential gcc-
aarch64-linux-gnu binutils-aarch64-linux-gnu nano libncurses5-dev lzop bc  
  
ENTRYPOINT ["/bin/bash"]  

