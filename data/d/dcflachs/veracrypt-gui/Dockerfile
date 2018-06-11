# Pull base image.  
FROM jlesage/baseimage-gui:debian-8  
  
MAINTAINER dcflachs  
  
#########################################  
## ENVIRONMENTAL CONFIG ##  
#########################################  
  
# User/Group Id gui app will be executed as default are 99 and 100  
ENV USER_ID=99  
ENV GROUP_ID=100  
  
ENV UMASK=000  
  
# Gui App Name default is "GUI_APPLICATION"  
ENV APP_NAME="VeraCrypt"  
  
# Default resolution, change if you like  
ENV DISPLAY_WIDTH=1280  
ENV DISPLAY_HEIGHT=720  
  
# Use a secure connection to the GUI  
ENV SECURE_CONNECTION 1  
  
# Clean tmp on startup  
ENV CLEAN_TMP_DIR 1  
  
#########################################  
## REPOSITORIES AND DEPENDENCIES ##  
#########################################  
RUN \  
add-pkg --virtual build-dependencies \  
wget ca-certificates && \  
echo 'deb
http://download.opensuse.org/repositories/home:/stevenpusser:/veracrypt/Debian_8.0/
/' > /etc/apt/sources.list.d/veracrypt.list && \  
wget -nv
https://download.opensuse.org/repositories/home:stevenpusser:veracrypt/Debian_8.0/Release.key
-O Release.key && \  
apt-key --keyring /etc/apt/trusted.gpg.d/veracrypt.gpg add - < Release.key &&
\  
rm Release.key && \  
del-pkg build-dependencies  
  
# Install packages needed for app  
RUN add-pkg --force-yes veracrypt ntfs-3g sudo  
  
# Copy X app start script to correct location  
COPY startapp.sh /startapp.sh  
  
# Copy default configuration file to correct location  
COPY Configuration.xml /defaults/Configuration.xml  
  
# Add veracrypt init script  
COPY veracrypt.sh /etc/cont-init.d/90-veracrypt.sh  
  
# Add veracrypt sudoers file  
RUN echo "$APP_USER ALL=(root) NOPASSWD:/usr/bin/veracrypt" >
/etc/sudoers.d/veracrypt  
RUN chmod 440 /etc/sudoers.d/veracrypt  
  
# Generate and install favicons.  
RUN \  
APP_ICON_URL=http://www.top-windows-tutorials.com/images/2013/04/veracrypt-
logo.png && \  
install_app_icon.sh "$APP_ICON_URL"  
  
#########################################  
## EXPORTS AND VOLUMES ##  
#########################################  
  
# Place whatever volumes and ports you want exposed here:  
VOLUME ["/mnt/containers"]  
VOLUME ["/mnt/disks"]  
  

