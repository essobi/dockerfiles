FROM pritunl/archlinux:2017-02-11  
MAINTAINER Charles Samborski <demurgos@demurgos.net>  
  
RUN pacman -S --noconfirm \  
bison \  
ca-certificates \  
cmake \  
flex \  
gcc \  
git \  
make \  
patch \  
python \  
sudo \  
valgrind  
  
ENV CXX gcc  
  
# Passwordless sudo for the user `developer`  
COPY sudoers /etc/sudoers  
RUN chmod 440 /etc/sudoers  
RUN groupadd sudo && useradd --create-home -G sudo -s /bin/bash developer  
  
RUN pacman -S --noconfirm fakeroot pkgbuild-introspection  
  
# USER developer  
RUN mkdir /src \  
&& git clone https://aur.archlinux.org/lcov.git /src/lcov \  
&& chown -R developer /src/lcov \  
&& su -l developer -c "cd /src/lcov && makepkg --noconfirm --syncdeps
--install && mksrcinfo"  
# && sudo makepkg --noconfirm --syncdeps --install  
CMD ["/bin/bash"]  

