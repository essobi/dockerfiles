# Docker-Version 0.9.1  
#  
# Version 0.1.0  
# Dockerizing Asp.Net vnext: Dockerfile for building a base for aspnetvnext
image.  
# Based on archlinux:latest, installs aspnet vnext following the instructions
from:  
# http://graemechristie.github.io/graemechristie/blog/2014/05/26/asp-dot-net-
vnext-on-osx-and-linux/  
FROM base/archlinux:latest  
MAINTAINER Saqib Rokadia  
  
ENV HOME /root  
RUN pacman --noconfirm -Syu unzip make autoconf libtool  
RUN cd /tmp && curl -qO http://download.mono-
project.com/sources/mono/mono-3.8.0.tar.bz2 && tar -xvf mono-3.8.0.tar.bz2 &&
rm ./mono-3.8.0.tar.bz2 && cd mono-3.8.0 && ./configure --prefix=/usr/local &&
make && make install && cd / && rm -r /tmp/mono-3.8.0  
  
ENV KRE_FEED https://www.myget.org/F/aspnetvnext/api/v2  
RUN mozroots --import --sync  
RUN printf "#\n# ~/.bashrc\n#\n" > ~/.bashrc  
RUN printf "# ~/.profile: executed by Bourne-compatible login shells.\n\nif [
"$BASH" ]; then\n if [ -f ~/.bashrc ]; then\n . ~/.bashrc\n fi\nfi\n\nmesg n"
> ~/.profile  
RUN curl https://raw.githubusercontent.com/aspnet/Home/dev/kvminstall.sh | sh
&& source ~/.kre/kvm/kvm.sh && kvm upgrade  
VOLUME ["/var/aspnet/"]  
  
# Expose port 80 from the container to the host  
EXPOSE 5000  
WORKDIR /var/aspnet  
ENTRYPOINT source ~/.kre/kvm/kvm.sh && kpm restore && cd src/web && k web  

