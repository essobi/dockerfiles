FROM pritunl/archlinux  
MAINTAINER Nicolas Senaud <nicolas@senaud.fr>  
  
ENV USER root  
  
RUN pacman -Syu --noconfirm && \  
pacman -S --noconfirm \  
base-devel \  
make \  
cmake \  
clang \  
boost \  
wget \  
gtest \  
opencv \  
git \  
zip \  
apr-util \  
python-pip \  
phonon-qt4 \  
phonon-qt4-vlc  
  
RUN useradd --no-create-home --shell=/bin/false yaourt && \  
usermod -L yaourt  
RUN mkdir -p /tmp/Package/ && \  
chown yaourt /tmp/Package  
  
RUN echo "export CC=clang" >> /etc/makepkg.conf && \  
echo "export CXX=clang++" >> /etc/makepkg.conf  
  
USER yaourt  
RUN (cd /tmp/Package && \  
wget https://aur.archlinux.org/cgit/aur.git/snapshot/log4cxx.tar.gz && \  
tar xzf log4cxx.tar.gz) && \  
(cd /tmp/Package/log4cxx && \  
makepkg)  
  
USER root  
RUN (cd /tmp/Package/log4cxx && \  
pacman -U --noconfirm log4cxx*.pkg.tar.xz)  
  
# cpp_redis installation  
RUN cd /tmp/ && \  
git clone https://github.com/Cylix/cpp_redis.git && \  
cd cpp_redis && \  
mkdir build && \  
cd build && \  
cmake -DCMAKE_INSTALL_PREFIX=/usr/local/ .. && \  
make install -j  
  
# Python dependencies  
RUN pip install jsonschema python-redis  
RUN pacman -S --noconfirm pyqt4-common  
  
# Cleanup and finalize  
RUN rm -rf \  
/tmp/* \  
/var/tmp/* && \  
mkdir /source  
  
VOLUME ["/source"]  
WORKDIR /source  
CMD ["/bin/bash"]  

