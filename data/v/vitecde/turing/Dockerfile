FROM ubuntu:16.04  
  
WORKDIR /tmp/ffmpeg  
  
RUN buildDeps="autoconf \  
automake \  
apt-utils \  
cmake \  
curl \  
g++ \  
gcc \  
git \  
make \  
nasm \  
perl \  
pkg-config \  
wget \  
ca-certificates" \  
&& apt-get -yqq update \  
&& apt-get install -yq \--no-install-recommends ${buildDeps} \  
&& mkdir -p /usr/src/ \  
&& git clone https://github.com/bbc/turingcodec.git /usr/src/turing \  
&& cd /usr/src/turing && git checkout stable \  
&& mkdir /usr/src/turing/build \  
&& cd /usr/src/turing/build \  
&& cmake -DCMAKE_INSTALL_PREFIX="/usr" -DCMAKE_BUILD_TYPE=Release ../ \  
&& make \  
&& make install \  
&& cd /usr/src/ && wget
https://sourceforge.net/projects/boost/files/boost/1.61.0/boost_1_61_0.tar.gz
\  
&& tar -xvzf boost_1_61_0.tar.gz \  
&& cd /usr/src/boost_1_61_0 \  
&& ./bootstrap.sh \--prefix=/usr \  
&& ./b2; echo "done" \  
&& cd /usr/src/boost_1_61_0 && ./b2 install; echo "done" \  
&& git clone https://github.com/kupix/FFmpeg-1.git -b libturing
/usr/src/ffmpeg \  
&& cd /usr/src/ffmpeg \  
&& ./configure \--prefix=/usr/ \--enable-libturing \--enable-gpl \--enable-
static \--disable-shared \  
&& make \  
&& make install \  
&& rm -rf /usr/src \  
&& apt-get purge -y ${buildDeps} \  
&& apt-get autoremove -y \  
&& apt-get clean -y \  
&& rm -rf /var/lib/apt/lists  
  
ENTRYPOINT ["ffmpeg"]  

