FROM apporc/arch-bootstrap  
  
MAINTAINER apporc <apporc@gmail.com>  
  
COPY packages/package-query-1.6.2-1-x86_64.pkg.tar.xz
packages/yaourt-1.6-1-any.pkg.tar.xz /  
  
RUN pacman -U --noconfirm /package-query-1.6.2-1-x86_64.pkg.tar.xz
/yaourt-1.6-1-any.pkg.tar.xz && \  
rm -rf /package-query-1.6.2-1-x86_64.pkg.tar.xz /yaourt-1.6-1-any.pkg.tar.xz  

