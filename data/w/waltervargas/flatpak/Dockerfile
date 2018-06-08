from debian:stretch  
LABEL maintainer "contact@walter.bio"  
  
ENV PACKAGES flatpak flatpak-builder  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y update && apt-get -y install
$PACKAGES && rm -rf /var/lib/apt/lists/*  

