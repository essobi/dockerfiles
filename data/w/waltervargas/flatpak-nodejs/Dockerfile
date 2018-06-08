from waltervargas/flatpak  
LABEL maintainer "contact@walter.bio"  
  
ENV PACKAGES nodejs  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y update && apt-get -y install
$PACKAGES && rm -rf /var/lib/apt/lists/*  

