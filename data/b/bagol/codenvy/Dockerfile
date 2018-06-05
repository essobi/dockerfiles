FROM bagol/archlinux  
RUN sed -i 's/#en_US/en_US/g' /etc/locale.gen && \  
locale-gen && echo 'LANG=en_US.UTF-8' > /etc/locale.conf  
ENV LANG en_US.UTF-8  
RUN pacman -S --noconfirm base-devel unzip curl  
RUN echo -e 'root ALL=(ALL) ALL\n %wheel ALL=(ALL) NOPASSWD: ALL' >
/etc/sudoers  
RUN groupadd -g 1000 user  
RUN useradd -g user -G wheel -m -s /bin/bash -u 1000 user  
  
USER user  
ENV LANG en_US.UTF-8  
ENV JAVA_HOME=/usr/lib/jvm/default  
ENV PATH=$PATH:/usr/lib/jvm/default/bin  
  
RUN cd /tmp && curl -O
https://aur.archlinux.org/cgit/aur.git/snapshot/jdk.tar.gz && \  
tar xf jdk.tar.gz && cd jdk && \  
makepkg --noconfirm --syncdeps --install  
  
EXPOSE 22 5000  
RUN sudo mkdir -p /projects && sudo chown user:user /projects  
WORKDIR /projects  
  
CMD tail -f /dev/null  
  
# vim: set ft=dockerfile:  

