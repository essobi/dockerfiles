FROM node:4.2.1  
# Set the locale  
# RUN locale-gen en_US.UTF-8  
# ENV LANG en_US.UTF-8  
# ENV LANGUAGE en_US:en  
# ENV LC_ALL en_US.UTF-8  
RUN echo deb http://archive.ubuntu.com/ubuntu precise universe multiverse >>
/etc/apt/sources.list; apt-get update; apt-get -y install autoconf automake
build-essential git mercurial cmake libass-dev libgpac-dev libtheora-dev
libtool libvdpau-dev libvorbis-dev pkg-config texi2html zlib1g-dev libmp3lame-
dev wget yasm libquvi*; apt-get clean  
  
# Run build script  
ADD ffmpeg/install.sh /install.sh  
RUN ["/bin/bash", "/install.sh"]  
  
CMD ["/bin/bash"]

