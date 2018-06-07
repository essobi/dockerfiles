FROM php:7  
MAINTAINER "Andrew Koebbe" <andrew.koebbe@gmail.com>  
  
# install doxygen dependencies  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get -y install graphviz && \  
rm -rf /var/lib/apt/lists/*  
  
# install doxygen  
RUN curl -sS
http://ftp.stack.nl/pub/users/dimitri/doxygen-1.8.11.linux.bin.tar.gz | tar
xvz --strip-components=2 -C /usr/local/bin/ doxygen-1.8.11/bin/  
  
# NOTE: must use json syntax process is not started in a subshell (and signals
are passed correctly)  
WORKDIR /src  
ENTRYPOINT ["/usr/local/bin/doxygen"]  

