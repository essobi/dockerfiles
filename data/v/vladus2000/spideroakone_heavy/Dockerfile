FROM vladus2000/arch-yaourt-evil-base  
MAINTAINER vladus2000 <docker@matt.land>  
  
COPY shiz/ /  
  
RUN pacman -Syyu --noconfirm && \  
su - evil -c 'yaourt -S --needed --noconfirm lftp python2-boto python2-dropbox
python2-gdata python2-gobject deja-dup duply borg openssh python-llfuse
spideroak-one' && \  
chmod +x /startup.sh /runit.sh && \  
rm -rf /var/cache/pacman/pkg/* /var/lib/pacman/sync/*  
  
CMD /bin/bash -c /startup.sh  
  

