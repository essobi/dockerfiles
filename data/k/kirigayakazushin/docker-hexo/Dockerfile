FROM base/archlinux  
  
MAINTAINER kirigayakazushin,<kirigaya@mkacg.com>  
RUN useradd -m -g users docker -G wheel  
RUN echo 'Server = https://mirrors.ustc.edu.cn/archlinux/$repo/os/$arch' >
/etc/pacman.d/mirrorlist  
RUN pacman -Sy git openssh nodejs npm --noconfirm  
RUN npm install hexo-cli -g  
RUN mkdir /Hexo  
RUN chown -R docker /Hexo  
VOLUME /Hexo  
WORKDIR /Hexo  
USER docker  
CMD ['/bin/bash']  

