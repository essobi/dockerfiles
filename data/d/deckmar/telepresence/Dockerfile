FROM centos  
  
RUN mkdir /app  
WORKDIR /app  
  
RUN yum -y update  
RUN yum -y install make libtool autoconf subversion git wget cmake gcc gcc-c++
pkgconfig nasm  
  
RUN git clone https://github.com/cisco/libsrtp/  
RUN cd libsrtp && git checkout v1.5.0 && CFLAGS="-fPIC" ./configure --enable-
pic && make && make install  
  
RUN wget http://www.openssl.org/source/openssl-1.0.2d.tar.gz  
RUN tar -xvzf openssl-1.0.2d.tar.gz  
RUN cd openssl-1.0.2d && ./config shared --prefix=/usr/local
\--openssldir=/usr/local/openssl && make && make install  
  
RUN yum -y install libogg-devel libvorbis-devel libtheora-devel  
  
RUN yum -y install speex-devel  
  
RUN wget http://www.tortall.net/projects/yasm/releases/yasm-1.2.0.tar.gz  
RUN tar -xvzf yasm-1.2.0.tar.gz  
RUN cd yasm-1.2.0 && ./configure && make && make install  
  
RUN yum -y install libvpx-devel  
  
RUN git clone git://opencore-amr.git.sourceforge.net/gitroot/opencore-
amr/opencore-amr  
RUN cd opencore-amr && autoreconf --install && ./configure && make && make
install  
  
RUN wget http://downloads.xiph.org/releases/opus/opus-1.0.2.tar.gz  
RUN tar -xvzf opus-1.0.2.tar.gz  
RUN cd opus-1.0.2 && ./configure --with-pic --enable-float-approx && make &&
make install  
  
RUN yum -y install gsm-devel  
  
RUN svn co http://g729.googlecode.com/svn/trunk/ g729b  
RUN cd g729b && ./autogen.sh && ./configure --enable-static --disable-shared
&& make && make install  
  
RUN svn co
http://doubango.googlecode.com/svn/branches/2.0/doubango/thirdparties/scripts/ilbc  
RUN cd ilbc && wget http://www.ietf.org/rfc/rfc3951.txt && awk -f extract.awk
rfc3951.txt && ./autogen.sh && ./configure && make && make install  
  
RUN wget ftp://ftp.videolan.org/pub/x264/snapshots/last_stable_x264.tar.bz2  
RUN yum -y install bzip2  
RUN tar -xvjf last_stable_x264.tar.bz2  
# the output directory may be difference depending on the version and date  
RUN cd x264-snapshot-* && ./configure --enable-shared --enable-pic && make &&
make install  
  
RUN yum -y install freetype-devel  
  
RUN wget http://downloads.sourceforge.net/faac/faac-1.28.tar.bz2  
RUN tar -xvjf faac-1.28.tar.bz2  
RUN cd faac-1.28 && sed -i.bak 's|char \\*strcasestr(const char \\*haystack,
const char \\*needle);|/\\* removed so that faac compiles correctly: & \\*/|g'
common/mp4v2/mpeg4ip.h  
RUN cd faac-1.28 && ./configure && make && make install  
  
# [1] checkout source code  
# [2] grap a release branch  
# [3] configure source  
# [4] build and install  
RUN git clone git://source.ffmpeg.org/ffmpeg.git ffmpeg  
RUN cd ffmpeg && git checkout n1.2 && ./configure \  
\--extra-cflags="-fPIC" \  
\--extra-ldflags="-lpthread" \  
\--enable-pic --enable-memalign-hack --enable-pthreads \  
\--enable-shared --disable-static \  
\--disable-network --enable-pthreads \  
\--disable-ffmpeg --disable-ffplay --disable-ffserver --disable-ffprobe \  
\--enable-gpl \  
\--disable-debug \  
\--enable-libfreetype \  
\--enable-libfaac \  
\--enable-nonfree \  
\--enable-libx264 --enable-encoder=libx264 --enable-decoder=h264 && make &&
make install  
  
RUN git clone https://github.com/cisco/openh264.git  
RUN cd openh264 && git checkout v1.1 && make ENABLE64BIT=Yes && make install  
  
RUN wget http://kcat.strangesoft.net/openal-releases/openal-
soft-1.15.1.tar.bz2  
RUN tar -xvjf openal-soft-1.15.1.tar.bz2  
RUN cd openal-soft-1.15.1/build && cmake .. && make && make install  
  
RUN yum -y install java-1.7.0-openjdk  
  
RUN svn checkout http://doubango.googlecode.com/svn/branches/2.0/doubango
doubango  
RUN cd doubango && ./autogen.sh && ./configure --with-speexdsp --with-ffmpeg
&& make && make install  
  
RUN ln -s /usr/lib64/libssl.so.1.0.1e /usr/lib64/libssl.so.1.0.0  
RUN ln -s /usr/lib64/libcrypto.so.1.0.1e /usr/lib64/libcrypto.so.1.0.0  
  
RUN svn checkout https://telepresence.googlecode.com/svn/trunk/ telepresence  
RUN cd telepresence && ./autogen.sh && ./configure && make && make install  
RUN echo "/usr/local/lib64" >> /etc/ld.so.conf.d/doubango.conf  
  
RUN yum install -y nano nc  
  
WORKDIR /app/telepresence  
  
EXPOSE 20060  
EXPOSE 20065  
EXPOSE 20066  
ADD ./telepresence.cfg /app/telepresence/telepresence.cfg  
  
CMD telepresence  

