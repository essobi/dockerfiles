FROM alpine:latest  
MAINTAINER William Weiskopf <william@weiskopf.me>  
  
ENV VERSION v0.5.1  
  
ENV CDRDAO_VERSION 1.2.3  
ENV PYCDDB_VERSION 0.1.4  
  
RUN apk add --no-cache \  
ca-certificates \  
cdparanoia \  
flac \  
libcdio \  
libsndfile \  
py-gobject \  
py-mutagen \  
py-musicbrainzngs \  
py-setuptools \  
sox \  
wget \  
&& apk add --no-cache --virtual=build-dependencies \  
g++ \  
gcc \  
gconf \  
git \  
libcdio-dev \  
libsndfile-dev \  
linux-headers \  
make \  
musl-dev \  
python-dev \  
py2-pip \  
swig \  
&& wget -O cdrdao.tar.bz2
http://downloads.sourceforge.net/cdrdao/cdrdao-$CDRDAO_VERSION.tar.bz2 \  
&& tar xf cdrdao.tar.bz2 \  
&& cd cdrdao* \  
&& sed -i '/ioctl.h/a #include <sys/stat.h>' dao/ScsiIf-linux.cc \  
&& sed -i 's/\(char .*REMOTE\)/unsigned \1/' dao/CdrDriver.h \  
&& sed -i 's/\(char .*REMOTE\)/unsigned \1/' dao/CdrDriver.cc \  
&& ./configure \  
&& make \  
&& make install \  
&& pip install pycdio \  
&& cd / \  
&& rm -r cdrdao* \  
&& wget -O pycddb.tar.gz
https://downloads.sourceforge.net/pycddb/pycddb-$PYCDDB_VERSION.src.tar.gz \  
&& tar xf pycddb.tar.gz \  
&& cd pycddb*/src \  
&& python setup.py install \  
&& cd / \  
&& rm -r pycddb* \  
&& git clone -b master --single-branch
https://github.com/JoeLametta/whipper.git \  
&& cd whipper/src \  
&& git checkout tags/$VERSION \  
&& make \  
&& make install \  
&& cd .. \  
&& python setup.py install \  
&& cd / \  
&& rm -r whipper \  
&& apk del build-dependencies \  
&& mkdir rips  
  
WORKDIR /rips  
  
#ENTRYPOINT 'whipper'  
  
#CMD ['cd', 'rip']  

