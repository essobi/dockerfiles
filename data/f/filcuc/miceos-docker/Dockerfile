from ubuntu:17.10  
RUN \  
apt-get update -y && \  
apt-get install -y xterm wget libglib2.0-0 libxkbcommon0 libdbus-1.3 build-
essential g++  
  
RUN \  
cd opt && \  
wget https://github.com/rm-hull/barebones-toolchain/archive/6.2.0.tar.gz && \  
tar -xf 6.2.0.tar.gz && \  
rm 6.2.0.tar.gz && \  
ln -s barebones-toolchain-6.2.0 toolchain  
  
RUN \  
cd opt && \  
wget https://cmake.org/files/v3.11/cmake-3.11.0-Linux-x86_64.tar.gz && \  
tar -xf cmake-3.11.0-Linux-x86_64.tar.gz && \  
rm cmake-3.11.0-Linux-x86_64.tar.gz && \  
ln -s cmake-3.11.0-Linux-x86_64 cmake  
  
RUN \  
cd /usr/bin && \  
wget https://raw.githubusercontent.com/benlau/qtci/master/bin/extract-qt-
installer && \  
chmod a+x extract-qt-installer  
  
RUN \  
cd /opt && \  
wget https://download.qt.io/official_releases/qtcreator/4.6/4.6.0/qt-creator-
opensource-linux-x86_64-4.6.0.run && \  
extract-qt-installer qt-creator-opensource-linux-x86_64-4.6.0.run
/opt/qtcreator-4.6 && \  
rm qt-creator-opensource-linux-x86_64-4.6.0.run && \  
ln -s qtcreator-4.6 qtcreator  
  
COPY cmake-toolchain-file.cmake /opt  
  
RUN useradd -u 1000 -ms /bin/bash developer  
  
RUN chown -R developer:developer /opt/  
  
RUN apt-get install -y gdb-multiarch qemu  
  
RUN apt-get install -y git sudo  
  
RUN echo "developer ALL=(ALL) ALL" >> /etc/sudoers  
  
RUN echo developer:developer | chpasswd  
  
USER developer  
WORKDIR /home/developer  
  
COPY config.tar.gz /home/developer  
RUN tar xf config.tar.gz && rm config.tar.gz  
  
USER root  
  
COPY chuid.sh /sbin  
RUN chmod o-rwx /sbin/chuid.sh && chmod u+rwx /sbin/chuid.sh  
  
CMD xterm

