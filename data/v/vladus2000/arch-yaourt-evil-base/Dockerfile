FROM archimg/base-devel  
MAINTAINER vladus2000 <docker@matt.land>  
  
COPY shiz/ /  
  
RUN echo >> /etc/pacman.conf && \  
echo '[aur-archlinux]' >> /etc/pacman.conf && \  
echo 'SigLevel = Never' >> /etc/pacman.conf && \  
echo 'Server = https://repo.itmettke.de/aur/$repo/$arch' >> /etc/pacman.conf
&& \  
pacman -Syyu \--noconfirm && \  
pacman -S \--needed \--noconfirm yaourt sudo vim bash-completion && \  
pacman -R \--noconfirm vi && \  
ln -sf /usr/bin/vim /usr/bin/vi && \  
ln -sf /usr/bin/vim /usr/bin/edit && \  
ln -sf /usr/bin/vim /usr/bin/ex && \  
ln -sf /usr/bin/vim /usr/bin/vedit && \  
ln -sf /usr/bin/vim /usr/bin/view && \  
echo alias 'cd..="cd .."' >> /etc/bash.bashrc && \  
echo alias 'l="ls -CF"' >> /etc/bash.bashrc && \  
echo alias 'la="ls -A"' >> /etc/bash.bashrc && \  
echo alias 'll="ls -alF"' >> /etc/bash.bashrc && \  
echo alias 'lld="ls -ald"' >> /etc/bash.bashrc && \  
echo alias 'lrt="ls -lrt"' >> /etc/bash.bashrc && \  
echo alias 'lrta="ls -lrta"' >> /etc/bash.bashrc && \  
echo alias 'netstat="ss"' >> /etc/bash.bashrc && \  
echo alias 'p="pgrep -af "' >> /etc/bash.bashrc && \  
useradd -G wheel evil && \  
mkdir ~evil && \  
chown evil ~evil && \  
echo '%wheel ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers && \  
chmod +x /*.sh && \  
rm -rf /var/cache/pacman/pkg/* /var/lib/pacman/sync/*  
  
CMD ["/bin/bash"]  

