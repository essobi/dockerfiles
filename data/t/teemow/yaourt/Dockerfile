FROM teemow/build  
  
RUN curl -O https://aur.archlinux.org/packages/pa/package-query/package-
query.tar.gz  
RUN tar zxvf package-query.tar.gz  
RUN cd package-query && makepkg -si --noconfirm  
  
RUN curl -O https://aur.archlinux.org/packages/ya/yaourt/yaourt.tar.gz  
RUN tar zxvf yaourt.tar.gz  
RUN cd yaourt && makepkg -si --noconfirm  

