FROM archimg/base  
MAINTAINER vladus2000 <docker@matt.land>  
  
COPY shiz/ /  
  
RUN \  
pacman -Syyu \--noconfirm && \  
pacman -S \--needed \--noconfirm vim bash-completion && \  
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
chmod +x /*.sh && \  
rm -rf /var/cache/pacman/pkg/* /var/lib/pacman/sync/*  
  
CMD ["/bin/bash"]  

