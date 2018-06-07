FROM escalade1/arch:latest  
  
MAINTAINER escalade  
  
# Create config directory  
RUN mkdir -p /root/.config  
  
# Copy packages to container  
COPY *.xz /tmp/  
  
# Install packages  
RUN pacman -U --noconfirm /tmp/*.xz  
RUN pacman -S --noconfirm python2-feedparser python2-pyopenssl  
  
# Remove downloaded packages  
RUN yes | pacman -Scc  

