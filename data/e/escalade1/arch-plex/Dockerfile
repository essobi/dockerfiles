FROM escalade1/arch:latest  
  
MAINTAINER escalade  
  
# Create config directory  
RUN mkdir -p /root/.config  
  
# Copy packages to container  
COPY *.xz /tmp/  
  
# Install packages  
RUN pacman -U --noconfirm /tmp/*.xz  

