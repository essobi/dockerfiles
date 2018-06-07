# Dockerfile for Banshee  
# Select base image  
FROM pritunl/archlinux:latest  
MAINTAINER doomsplayer@gmail.com  
  
RUN pacman -Sy --noconfirm abs elixir binutils base-devel sudo \  
&& abs community/erlang-nox \  
&& sed -ri '$ibuilder ALL = (ALL) NOPASSWD: ALL' /etc/sudoers \  
&& useradd -m builder  
  
USER builder  
  
RUN cp -r /var/abs/community/erlang-nox /home/builder/  
  
WORKDIR /home/builder/erlang-nox  
  
COPY PKGBUILD .  
  
RUN makepkg -s --noconfirm \  
&& sudo pacman -U erlang-nox-*-x86_64.pkg.tar.xz --noconfirm \  
&& sudo userdel -r builder  
  
USER root  

