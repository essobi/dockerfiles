FROM ubuntu:12.04  
  
RUN apt-get update && \  
apt-get install -y python-software-properties \  
software-properties-common \  
sudo bc \  
git texinfo gnupg flex bison gperf \  
build-essential zip curl libc6-dev libncurses5-dev:i386 \  
x11proto-core-dev libx11-dev:i386 \  
libreadline6-dev:i386 libgl1-mesa-glx:i386 \  
libgl1-mesa-dev g++-multilib mingw32 tofrodos \  
python-markdown libxml2-utils xsltproc zlib1g-dev:i386 \  
gcc g++ autoconf pkg-config libtool libltdl7-dev \  
texlive texlive-extra-utils libglib2.0-dev xutils-dev \  
xmlto xfig ragel gtk-doc-tools intltool fdupes \  
libcap2-bin cmake ninja-build autopoint \  
libc6-dev:i386 libogg-dev \  
liblzma-dev libcap-dev libgcrypt-dev \  
libexpat1-dev libnspr4-0d:i386 libcap-dev \  
libdbus-glib-1-2  
  
RUN apt-get install -y libsdl1.2-dev  
  
RUN add-apt-repository -y ppa:openjdk-r/ppa && apt-get update && apt-get
install -y openjdk-8-jdk  
  
ENV USER=root  
  
COPY repo /bin/repo  
  
RUN chmod a+x /bin/repo  
  
RUN useradd -c 'container user' -u 1000 -g 0 appuser; mkdir -p /home/appuser;
cp /root/.bashrc /home/appuser/ ; cp /root/.profile /home/appuser/ ;chown -R
appuser /home/appuser;  

