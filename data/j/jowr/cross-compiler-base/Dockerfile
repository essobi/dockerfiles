FROM debian:stable  
MAINTAINER Matt McCormick "matt.mccormick@kitware.com"  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get -y --no-install-recommends install \  
automake \  
autogen \  
bash \  
build-essential \  
bzip2 \  
ca-certificates \  
curl \  
file \  
git \  
gzip \  
libcurl4-openssl-dev \  
libssl-dev \  
make \  
ncurses-dev \  
pkg-config \  
python \  
rsync \  
runit \  
sed \  
tar \  
vim \  
wget \  
xz-utils  
  
# Build and install CMake from source.  
WORKDIR /usr/src  
RUN git clone git://cmake.org/cmake.git CMake && \  
cd CMake && \  
git checkout release  
RUN mkdir CMake-build  
WORKDIR /usr/src/CMake-build  
RUN /usr/src/CMake/bootstrap \  
\--parallel=$(nproc) \  
\--prefix=/usr && \  
make -j$(nproc) && \  
./bin/cmake -DCMAKE_USE_SYSTEM_CURL:BOOL=ON \  
-DCMAKE_USE_OPENSSL:BOOL=ON . && \  
make install && \  
rm -rf *  
WORKDIR /usr/src  
  
# Build and install Ninja from source  
RUN git clone https://github.com/martine/ninja.git && \  
cd ninja && \  
git checkout release && \  
python ./configure.py --bootstrap && \  
./ninja && \  
cp ./ninja /usr/bin/  
  
WORKDIR /usr/src  
RUN rm -rf CMake* ninja  
RUN dpkg --purge \  
autogen \  
ca-certificates \  
file \  
git \  
libcurl4-openssl-dev \  
libssl-dev \  
ncurses-dev \  
rsync && apt-get -y clean && apt-get -y autoremove  
  
WORKDIR /build  
ENTRYPOINT ["/dockcross/entrypoint.sh"]  
  
COPY imagefiles/entrypoint.sh imagefiles/dockcross /dockcross/  

