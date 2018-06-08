FROM openjdk:8  
LABEL maintainer="salvianreynaldi@gmail.com"  
  
ENV USER=lineageos \  
HOME_DIR=/home/lineageos  
# ccache specifics  
ENV CCACHE_SIZE=50G \  
CCACHE_DIR=$HOME_DIR/ccache \  
USE_CCACHE=1 \  
# Extra include PATH, it may not include /usr/local/(s)bin on some systems  
PATH=$PATH:/usr/local/bin/  
  
RUN export DEBIAN_FRONTEND=noninteractive \  
&& apt update \  
&& apt dist-upgrade -y \  
&& apt install -y --no-install-recommends \  
# Install build dependencies (source:
https://wiki.lineageos.org/devices/sagit/build)  
bc \  
bison \  
build-essential \  
ccache \  
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
pngcrush \  
rsync \  
schedtool \  
squashfs-tools \  
xsltproc \  
zip \  
zlib1g-dev \  
unzip \  
# Install additional packages which are useful for building Android  
android-sdk-platform-tools-common \  
android-tools-adb \  
android-tools-fastboot \  
bash-completion \  
bsdmainutils \  
file \  
nano \  
python \  
tmux \  
sudo \  
wget \  
htop \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /var/tmp/* /tmp/*  
  
RUN set -ex ;\  
groupadd -r lineageos && useradd -r -g lineageos lineageos && usermod -u 1000
lineageos ;\  
echo "lineageos ALL=NOPASSWD: ALL" >> /etc/sudoers.d/lineageos ;  
RUN curl https://storage.googleapis.com/git-repo-downloads/repo >
/usr/local/bin/repo \  
&& chmod a+x /usr/local/bin/repo  
  
USER $USER  
WORKDIR $HOME_DIR  
ENTRYPOINT /bin/bash  
CMD ["-eo", "pipefail"]  

