# ZNC with buildmod enabled.  
#  
# (See README.md for instructions.)  
FROM debian:jessie  
MAINTAINER Andrey Petrov <andrey.petrov@shazow.net>  
  
RUN apt-get update && apt-get install -y \  
ca-certificates \  
znc \  
\--no-install-recommends  
  
# Extra stuff for znc-buildmod (can remove if we don't care about building
modules)  
RUN apt-get install -y \  
build-essential \  
libcurl4-openssl-dev \  
znc-dev \  
\--no-install-recommends  
  
# Make user  
RUN useradd --create-home znc  
USER znc  
WORKDIR /home/znc  
  
VOLUME ["/home/znc/.znc"]  
CMD ["znc", "-f"]  

