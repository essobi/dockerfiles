FROM debian:stretch  
  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get -y --no-install-
recommends install \  
inkscape  
  
WORKDIR /document  
ENTRYPOINT ["inkscape"]  

