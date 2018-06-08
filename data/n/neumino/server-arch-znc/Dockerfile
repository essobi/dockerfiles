FROM base/arch:latest  
MAINTAINER: Michel Tu <orphee@gmail.com>  
  
RUN pacman -Syu --noconfirm  
RUN pacman -S znc --noconfirm  
  
CMD ["znc", "-f", "--allow-root", "-d", "/root/znc"]  
  
EXPOSE 5500  

