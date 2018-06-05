FROM alpine  
RUN wget http://archlinux.cs.nctu.edu.tw/iso/2017.02.01/archlinux-
bootstrap-2017.02.01-x86_64.tar.gz -O - | tar -zx && \  
cp -a /root.x86_64/* . || rm -rf /root.x86_64 && \  
ln -s /usr/bin/bash /bin/bash  
  
ADD mirrorlist /etc/pacman.d/  
  
RUN pacman-key --init && \  
pacman-key --populate archlinux && \  
pacman -Syu --noconfirm && \  
pacman -S tar wget --noconfirm --force && \  
yes|pacman -Scc  
  
CMD ["/bin/bash"]  

