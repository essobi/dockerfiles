FROM ubuntu:16.04  
MAINTAINER jdb  
  
ENV CALDERA /tmp/caldera/  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV LC_ALL C  
  
USER root  
RUN apt-get -qq update && \  
apt-get install -qq -y \  
build-essential \  
git \  
python3-dev \  
mongodb \  
python3-pip \  
crudini \  
wget \  
supervisor  
  
RUN pip3 install --upgrade setuptools  
  
RUN git clone https://github.com/mitre/caldera $CALDERA  
  
RUN pip3 install -r $CALDERA/caldera/requirements.txt  
  
  
#systemctl restart mongodb  
  
  
RUN mkdir -p $CALDERA/dep/crater/crater && \  
wget -O $CALDERA/dep/crater/crater/CraterMain.exe
https://github.com/mitre/caldera-
crater/releases/download/v0.1.0/CraterMainWin7.exe  
  
  
RUN apt-get -qq -y clean & \  
apt-get remove -qq -y \  
binutils \  
build-essential \  
bzip2 \  
cpp \  
cpp-5 \  
debfoster \  
dpkg-dev \  
fakeroot \  
g++ \  
g++-5 \  
gcc \  
gcc-5 \  
git \  
git-man \  
libalgorithm-diff-perl \  
libalgorithm-diff-xs-perl \  
libalgorithm-merge-perl \  
libbsd0 \  
libc-dev-bin \  
libc6-dev \  
libcc1-0 \  
libdpkg-perl \  
libedit2 \  
liberror-perl \  
libexpat1-dev \  
libfakeroot \  
libfile-fcntllock-perl \  
libgc1c2 \  
libgcc-5-dev \  
libisl15 \  
libmpc3 \  
libmpfr4 \  
libperl5.22 \  
libpython3-dev \  
libpython3.5-dev \  
libstdc++-5-dev \  
libx11-6 \  
libx11-data \  
libxau6 \  
libxcb1 \  
libxdmcp6 \  
libxext6 \  
libxmuu1 \  
linux-libc-dev \  
make \  
makedev \  
manpages \  
manpages-dev \  
openssh-client \  
patch \  
perl \  
perl-modules-5.22 \  
rename \  
rsync \  
xauth  
  
RUN apt-get autoremove -y && \  
rm -rf /root/.cache  
  
RUN useradd caldera  
  
  
EXPOSE 8888  
COPY supervisord.conf /etc/supervisor/conf.d/caldera.conf  
  
RUN chown -R caldera /tmp/caldera/  
  
ADD firstboot.sh /firstboot.sh  
RUN touch /firstboot.tmp  
  
  
ENTRYPOINT /usr/bin/supervisord -c /etc/supervisor/supervisord.conf  

