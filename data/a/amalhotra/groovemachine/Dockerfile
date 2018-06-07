FROM centos:7  
MAINTAINER Amit Malhotra <amit08@gmail.com>  
  
# Set US locale (localegen on ubuntu)  
RUN localedef --quiet -c -i en_US -f UTF-8 en_US.UTF-8  
ENV LANGUAGE en_US  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
ENV C_FORCE_ROOT true  
  
RUN yum clean all && \  
yum update -y && \  
yum install -y epel-release && \  
yum install -y http://li.nux.ro/download/nux/dextop/el7/x86_64/nux-dextop-
release-0-5.el7.nux.noarch.rpm && \  
yum groupinstall -y "Development tools" && \  
yum install -y python-pip \  
python34.x86_64 \  
python34-devel.x86_64 \  
python-devel \  
nodejs \  
npm \  
cmake \  
unzip \  
wget \  
GraphicsMagick \  
ffmpeg \  
ffmpeg-devel \  
libchromaprint \  
fftw3 \  
compat-glibc-headers  
  
# Install pip for python3  
# RUN ln -s /usr/bin/python3.4 /usr/bin/python3  
RUN curl https://bootstrap.pypa.io/get-pip.py | python3 -  
  
# Install supervisor  
RUN pip2 install supervisor  
RUN mkdir /var/log/supervisor  
  
#### libgroove installation ####  
WORKDIR /root  
# update cmake  
RUN wget
https://kojipkgs.fedoraproject.org/packages/cmake/2.8.12/3.fc21/src/cmake-2.8.12-3.fc21.src.rpm  
RUN yum-builddep -y cmake-2.8.12-3.fc21.src.rpm  
RUN rpmbuild --rebuild cmake-2.8.12-3.fc21.src.rpm  
RUN cd rpmbuild/RPMS/x86_64 && rpm -Uvh cmake-2.8.12-3.el7.centos.x86_64.rpm  
  
# install speexdsp library  
RUN wget http://downloads.xiph.org/releases/speex/speexdsp-1.2rc3.tar.gz && \  
tar xzf speexdsp-1.2rc3.tar.gz  
RUN cd speexdsp-1.2rc3 && \  
./configure && \  
make && \  
make install  
  
# install libebur  
ENV PKG_CONFIG_PATH /usr/local/lib/pkgconfig  
RUN git clone https://github.com/jiixyj/libebur128.git  
RUN cd libebur128 && \  
mkdir build && \  
cd build && \  
cmake .. && \  
make && \  
make install  
  
# install libsoundio  
RUN wget http://libsound.io/release/libsoundio-1.0.3.tar.gz && \  
tar xzf libsoundio-1.0.3.tar.gz  
RUN cd libsoundio-1.0.3 && \  
mkdir build && \  
cd build && \  
cmake .. && \  
make && \  
make install  
  
# install libchromaprint  
ENV FFTW3_DIR /usr/lib64  
RUN wget
https://bitbucket.org/acoustid/chromaprint/downloads/chromaprint-1.1.tar.gz &&
\  
tar xzf chromaprint-1.1.tar.gz  
RUN cd chromaprint-1.1 && \  
cmake . && \  
make && \  
make install  
  
# install libsdl  
RUN cd /usr/include && \  
ln -s ffmpeg/* .  
RUN wget http://www.libsdl.org/release/SDL2-2.0.3.tar.gz && \  
tar -zxf SDL2-2.0.3.tar.gz  
RUN cd SDL2-2.0.3 && \  
./configure && \  
make all && \  
make install  
  
# install libgroove  
RUN git clone https://github.com/andrewrk/libgroove.git && \  
cd libgroove && \  
git checkout tags/4.3.0  
RUN cd libgroove && \  
mkdir build && \  
cd build && \  
cmake .. && \  
make && \  
make install  
  
RUN echo "/usr/local/lib" > /etc/ld.so.conf.d/usrlocal.conf && \  
ldconfig -v  
  
# Setup the system for requirements installation  
COPY templates/etc/supervisord.conf /etc/supervisord.conf  
  
WORKDIR /tmp  
COPY dependencies.txt /tmp/dependencies.txt  
RUN pip3 install -r dependencies.txt  
  
COPY dependencies.dev.txt /tmp/dependencies.dev.txt  
RUN pip3 install -r dependencies.dev.txt  
  
RUN mkdir -p /opt/apps/env && \  
ln -s /usr/bin/python3 /opt/apps/env/python  
ENV PATH
/opt/apps/env:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin  

