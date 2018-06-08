FROM registry.fedoraproject.org/fedora:28  
MAINTAINER Marco Cyriacks <marco@cyriacks.net>  
  
RUN dnf -y upgrade  
RUN dnf install -y git make fedora-packager fedora-review gcc-c++
libstdc++-devel  
RUN dnf install -y qt5-qtbase-devel qt5-qtwebkit-devel qt5-qtsvg-devel
libmarkdown-devel  
  
# Set correct timezone  
ENV TZ=Europe/Berlin  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone  
  

