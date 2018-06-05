FROM pritunl/archlinux  
MAINTAINER plimanowski+dev@protonmail.com  
  
RUN mkdir /app  
WORKDIR /app  
  
RUN pacman -Syu --noconfirm dosfstools parted make &&\  
pacman -Sc --noconfirm  
  
ADD Makefile /app/  
  
ENTRYPOINT ["make"]  
CMD ["copy"]  

