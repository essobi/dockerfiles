#  
# ArchLinux + Packaging tools  
#  
FROM base/archlinux  
  
LABEL maintainer="s@sfuhrm.de"  
  
RUN pacman -Sy && \  
pacman -S --noconfirm binutils fakeroot jdk8-openjdk maven apache-ant gradle
&& \  
pacman -Scc && \  
useradd -m capsula  
  
WORKDIR /  
  
CMD bash  

