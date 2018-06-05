FROM pritunl/archlinux:2018-06-02  
RUN pacman -Syu --noconfirm  
RUN pacman -Sy --noconfirm sudo base-devel gettext cmake git ninja boost
libsodium wget python openssl qt5-base qt5-imageformats qt5-xcb-private-
headers openal ffmpeg opus zlib clang python-pip  
RUN pip install conan  
RUN echo "nobody ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers  
RUN pacman -Sy ccache --noconfirm  
RUN (echo "y"; echo "y") | pacman -Scc  
  
#RUN mkdir /build  
#RUN cd /build  
#RUN wget https://raw.githubusercontent.com/berkus/llvm-
build/master/build_toolchain.sh  
#RUN sh build_toolchain.sh  
# Put Clang ahead in the PATH search  
#ENV PATH="/usr/local/opt/llvm:${PATH}"  
# Location where travis config stored  
ENV TRAVIS_CONFIG_PATH /travis  
VOLUME /travis  
  
# Generally the current working dir will be used as the repo volume  
VOLUME /repo  
WORKDIR /repo  

