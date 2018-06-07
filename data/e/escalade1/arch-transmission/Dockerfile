FROM escalade1/arch:latest  
  
MAINTAINER escalade  
  
# Create config directory  
RUN mkdir -p /root/.config  
  
# Install Transmission  
RUN pacman -Sy --noconfirm transmission-cli  
  
# Remove downloaded packages  
RUN yes | pacman -Scc  

