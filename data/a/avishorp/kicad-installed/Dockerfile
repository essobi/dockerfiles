# Dockerfile for KiCAD  
FROM avishorp/kicad-built  
  
CMD ["/usr/local/bin/kicad"]  
  
# Install everything  
RUN make -C /build/kicad.bzr/build install  
RUN make -C /build/kicad-library.bzr/build install  
  
# Cleanup  
RUN rm -fr /build  
RUN apt-get purge -y build-essential bzr bzrtools checkinstall cmake doxygen
zlib1g-dev libwebkitgtk-dev \  
libglew-dev libcairo2-dev libbz2-dev libssl-dev swig libwxbase3.0-dev
libwxgtk3.0-dev  
RUN apt-get clean && rm -fr /var/libs/apt/lists/* /tmp/* /var/tmp/*  
  
VOLUME /tmp/.X11-unix /tmp/.X11-unix  
ENV DISPLAY :0  

