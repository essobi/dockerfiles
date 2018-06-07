FROM escalade1/arch:latest  
  
MAINTAINER escalade  
  
# Install pcsx2  
RUN yes | pacman -Sy pcsx2-git lib32-libglvnd nvidia lib32-nvidia-utils ttf-
dejavu  
  
# Remove downloaded packages  
RUN yes | pacman -Scc  

