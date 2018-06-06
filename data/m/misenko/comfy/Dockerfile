FROM finalduty/archlinux  
MAINTAINER Michal Kimle <kimle.michal@gmail.com>  
  
ENV COMFY_VERSION 0.2.14  
ENV COMFY_DIR /data  
  
# update + dependencies  
RUN pacman -Syu --noconfirm && pacman -S --noconfirm wget git unzip fakeroot
binutils qemu-headless  
  
# install ruby-2.3.3  
RUN wget
https://archive.archlinux.org/packages/r/ruby/ruby-2.3.3-2-x86_64.pkg.tar.xz
&& pacman -U --noconfirm ruby-*-x86_64.pkg.tar.xz  
  
# user  
RUN useradd -m -G wheel -s /bin/bash comfy  
USER comfy  
  
# packer  
RUN cd && wget https://aur.archlinux.org/cgit/aur.git/snapshot/packer-
io.tar.gz && tar -zxf packer-io.tar.gz && cd packer-io && makepkg  
USER root  
RUN pacman -U --noconfirm /home/comfy/packer-io/packer-io-*-x86_64.pkg.tar.xz  
RUN ln -s /usr/bin/packer-io /usr/bin/packer  
  
# comfy  
RUN gem install comfy -v $COMFY_VERSION  
  
# volume  
RUN mkdir -p $COMFY_DIR  
VOLUME ["$COMFY_DIR"]  
  
# locales  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
# ruby gems access  
ENV PATH=$PATH:/root/.gem/ruby/2.3.0/bin  
  
ENTRYPOINT ["comfy"]  

