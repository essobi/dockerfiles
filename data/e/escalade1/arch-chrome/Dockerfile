FROM escalade1/arch:latest  
  
MAINTAINER escalade  
  
# Create config directory  
RUN mkdir -p /root/.config  
  
# Set default Chrome arguments  
RUN echo "--no-sandbox --test-type --start-maximized --user-data-
dir=/root/.config/google-chrome" > /root/.config/chrome-flags.conf  
  
# Install Chrome  
RUN pacman -Sy --noconfirm libexif google-chrome ttf-tlwg ttf-linux-libertine  
  
# Remove downloaded packages  
RUN yes | pacman -Scc  

