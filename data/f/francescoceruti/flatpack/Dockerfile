FROM ubuntu:18.04  
  
ARG DEBIAN_FRONTEND=noninteractive  
RUN apt-get update && apt-get install -y apt-utils  
  
# Add alexlarsson/flatpak ppa  
RUN apt-get update && apt-get install -y \  
software-properties-common \  
python3-software-properties \  
&& add-apt-repository -y \  
ppa:alexlarsson/flatpak \  
&& apt-get purge -y \  
software-properties-common \  
python3-software-properties \  
&& apt-get autoremove -y  
  
# Install flatpak  
RUN apt-get update && apt-get install -y \  
flatpak \  
flatpak-builder \  
&& rm -rf /var/lib/apt/lists/*  

