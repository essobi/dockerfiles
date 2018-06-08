# automatic building on push is not activated (i expect the dockerfile to
change rarely)  
FROM dock0/arch  
MAINTAINER Leander Kurscheidt  
  
RUN pacman -Syy  
RUN pacman -S base-devel git systemd openssh cmake meson ninja protobuf-c
check --noconfirm  
  
RUN useradd tester  
RUN useradd spawny  
RUN echo 'tester:tester-password' | chpasswd  

