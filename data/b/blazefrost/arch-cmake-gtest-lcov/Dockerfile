FROM base/devel:latest  
  
# DONT refresh the system - this is bad because of COW  
# See https://docs.docker.com/engine/userguide/eng-image/dockerfile_best-
practices/#run  
# Only sync the package database  
# AND prepare the build environment  
# AND fetch, build and install lcov  
# AND cleanup  
RUN pacman -Sy && \  
pacman -S --noconfirm --needed gtest doxygen cmake git && \  
\  
pushd . && \  
cd /tmp && \  
curl -o lcov.tar.gz
https://aur.archlinux.org/cgit/aur.git/snapshot/lcov.tar.gz && \  
tar xf lcov.tar.gz && \  
rm lcov.tar.gz && \  
chmod a+w lcov && \  
cd lcov && \  
su -c "makepkg" -s /bin/bash nobody && \  
pacman --noconfirm -U `find . -name '*.tar.xz'` && \  
cd .. && \  
rm -rf lcov && \  
popd && \  
\  
rm -rf /var/cache/pacman/pkg/  

