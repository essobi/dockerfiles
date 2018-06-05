# Builds a docker gui image  
FROM hurricane/dockergui:xvnc  
  
#########################################  
## ENVIRONMENTAL CONFIG ##  
#########################################  
# Set environment variables  
ENV HOME /home/demonsaw  
  
# User/Group Id gui app will be executed as default are 99 and 100  
ENV USER_ID=99  
ENV GROUP_ID=100  
# Gui App Name default is "Demonsaw 4.0.3"  
ENV APP_NAME="Demonsaw 4.0.3"  
# Default resolution, change if you like  
ENV WIDTH=1280  
ENV HEIGHT=720  
# Use baseimage-docker's init system  
CMD ["/sbin/my_init"]  
  
#########################################  
## REPOSITORIES AND DEPENDENCIES ##  
#########################################  
RUN echo 'deb http://archive.ubuntu.com/ubuntu trusty main universe
restricted' > /etc/apt/sources.list && \  
echo 'deb http://archive.ubuntu.com/ubuntu trusty-updates main universe
restricted' >> /etc/apt/sources.list && \  
add-apt-repository ppa:ubuntu-toolchain-r/test && \  
apt-get update && \  
apt-get install -y \  
curl \  
libxcb-glx0 \  
libX11-xcb1 \  
libX11-xcb-dev \  
libxi6 \  
libstdc++6 \  
libfontconfig1 \  
libXrender1 \  
libglib2.0-0 \  
libgl1-mesa-dev && \  
rm -rf /var/lib/apt/lists/* && \  
mkdir -p /home/demonsaw/downloads && \  
curl -SL https://www.demonsaw.com/download/demonsaw_nix_64.tar.gz \  
| tar xvz -C /home/demonsaw && \  
chown -R nobody:users $HOME && \  
chmod 0755 /home/demonsaw/Demonsaw  
  
# Install packages needed for app  
#########################################  
## GUI APP INSTALL ##  
#########################################  
# Install steps for X app  
ENV QT_XKB_CONFIG_ROOT /usr/share/X11/xkb  
  
# Copy X app start script to right location  
COPY start.sh /startapp.sh  
  
#########################################  
## EXPORTS AND VOLUMES ##  
#########################################  
# Place whatever volumes and ports you want exposed here:  

