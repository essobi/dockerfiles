FROM escalade1/arch:latest  
  
MAINTAINER escalade  
  
#add user to install libvlc  
RUN useradd --no-create-home --shell=/bin/false build && usermod -L build  
RUN echo "build ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers  
RUN echo "root ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers  
  
# Install packages  
RUN pacman -Sy --noconfirm base-devel wget bc gperf zip xorg-mkfontscale xorg-
mkfontdir xorg-bdftopcf libxslt jre8-openjdk-headless perl-xml-parser git
unzip python patchutils lzop perl-json svn xa kodi-tools-texturepacker vlc  
  
# LibreELEC Docker addon expects this go path  
RUN ln -s /usr/lib/go /usr/lib/golang  
  
# Remove downloaded packages  
RUN yes | pacman -Scc  
  

