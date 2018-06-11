FROM ubuntu:16.04  
# ia32-libs \ # pkg not found for xenial: has no installation candidate  
# libglu1-mesa:i386 \ # pkg not found for xenial  
# libglu1-mesa:amd64 \ Fix libGL.so.1 not found  
# dbus-x11 \  
# libxext-dev \  
# libxrender-dev \  
# libxtst-dev \  
# flashplugin-installer \ # pkg not found for xenial  
# adobe-flashplugin \ # pkg not found for xenial: has no installation
candidate  
# ubuntu-restricted-extras \ # pkg not found for xenial  
RUN apt-get update && \  
apt-get install -y \  
\--no-install-recommends \  
sudo \  
libglu1-mesa:amd64 \  
dbus-x11 \  
libxext-dev \  
libxrender-dev \  
libxtst-dev \  
fonts-noto-cjk \  
firefox && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
ENV USER ubuntu  
ENV UID 1000  
RUN useradd -m -u $UID $USER && \  
echo "$USER ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers  
  
ADD docker-entrypoint.sh /  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD ["/usr/bin/firefox"]  

