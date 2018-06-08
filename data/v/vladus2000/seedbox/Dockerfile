FROM vladus2000/rutorrent  
MAINTAINER vladus2000 <docker@matt.land>  
  
COPY shiz/ /home/evil/shiz/  
  
RUN \  
su - evil -c 'yaourt -Syyu \--needed \--noconfirm && yaourt -S \--needed
\--noconfirm flac lame mp3gain sox vorbis-tools vorbisgain whatmp3
python2-notify python2-babel python2-cheetah python2-mako jackett python2-pip
wget rsync unzip unrar p7zip zip openssh rar' && \  
pacman -U \--needed \--noconfirm
https://archive.archlinux.org/packages/p/python2/python2-2.7.12-2-x86_64.pkg.tar.xz
&& \  
pacman -S \--needed \--noconfirm openssl-1.0 && \  
chown -R evil ~evil/shiz && \  
su - evil -c 'mkdir -p ~/sickrage && mkdir -p ~/.config/Jackett && cp
~/shiz/ServerConfig.json ~/.config/Jackett' && \  
su - evil -c 'git clone https://github.com/SiCKRAGETV/SiCKRAGE.git SickRage &&
cp ~/shiz/config.ini ~/sickrage' && \  
cd /home/evil/SickRage && \  
pip2 install -r requirements.txt && \  
su - evil -c 'git clone https://github.com/CouchPotato/CouchPotatoServer.git
&& mkdir ~/.couchpotato && cp ~/shiz/settings.conf ~/.couchpotato/.' && \  
cp ~evil/shiz/startup.sh / && \  
chmod +x /startup.sh && \  
rm -rf /var/cache/pacman/pkg/* /var/lib/pacman/sync/*  
  
EXPOSE 8069  
EXPOSE 49152  
  
CMD /bin/bash -c /startup.sh  
  
VOLUME /home/evil/downloads  
VOLUME /home/evil/sickrage  
VOLUME /home/evil/.couchpotato  
VOLUME /home/evil/.config/Jackett  

