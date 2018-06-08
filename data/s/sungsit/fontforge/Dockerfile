#  
# FontForge (on Archlinux)  
#  
FROM nfnty/arch-mini  
  
MAINTAINER Sungsit Sawaiwan  
  
ENV version=20150720 user=fontdev  
ENV home=/home/$user \  
sudofile=/etc/sudoers.d/$user \  
srcdir=/home/$user/src  
  
# Change mirrors, sync & install required packages  
#COPY config/mirrorlist /etc/pacman.d/  
RUN pacman -Syy --noc \  
&& pacman -S --noc sudo fontforge bdf-unifont \  
  
&& useradd --create-home --home-dir $home $user \  
&& echo $user " ALL=(ALL:ALL) NOPASSWD:ALL" > $sudofile \  
&& chmod 600 $sudofile \  
&& find /var/cache/pacman/pkg -mindepth 1 -delete  
  
# Copy config files  
COPY config/local.conf /etc/fonts/  
COPY config/.bashrc $home/  
RUN chown -R $user:$user $home  
# Set default command & working dir for fontdev user.  
USER $user  
WORKDIR $home  
CMD [ "fontforge" ]  
  
#  
# Build command:  
# docker build -t "sungsit/fontforge:archlinux" .  
#  

