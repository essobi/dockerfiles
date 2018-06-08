FROM ubuntu:xenial  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
bc \  
bison \  
build-essential \  
curl \  
flex \  
g++-multilib \  
gcc-multilib \  
git \  
gnupg \  
gperf \  
imagemagick \  
lib32ncurses5-dev \  
lib32readline-dev \  
lib32z1-dev \  
libesd0-dev \  
liblz4-tool \  
libncurses5-dev \  
libsdl1.2-dev \  
libssl-dev \  
libwxgtk3.0-dev \  
libxml2 \  
libxml2-utils \  
lzop \  
openjdk-8-jdk \  
pngcrush \  
repo \  
rsync \  
schedtool \  
squashfs-tools \  
xsltproc \  
unzip \  
zip \  
zlib1g-dev  
  
ENV ANDROID_JACK_VM_ARGS="-Dfile.encoding=UTF-8 -XX:+TieredCompilation -Xmx4G"  
ENV CCACHE_COMPRESS=1  
ENV USE_CCACHE=1  
ENV CCACHE_DIR=/var/ccache  
  
RUN useradd -m -u 1000 lineage  
  
VOLUME /var/lineage  
VOLUME /var/ccache  
  
WORKDIR /var/lineage  
ENV USER=lineage  
USER ${USER}  
  
ENTRYPOINT ["/bin/bash"]  

