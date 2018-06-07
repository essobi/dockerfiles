FROM ubuntu:wily  
  
ENV BOOST_DIR /tmp/boost_1_59_0  
ENV GCCVERSION 4.2  
ENV MINGW_COMPILER i686-w64-mingw32-g++  
  
# Install dependencies  
RUN apt-get -y update && apt-get -y install \  
bzip2 \  
g++ \  
gcc-multilib \  
g++-multilib \  
g++-mingw-w64-i686 \  
make \  
wget \  
&& apt-get clean && apt-get purge  
  
# Download boost library  
RUN wget -P /tmp/
http://downloads.sourceforge.net/project/boost/boost/1.59.0/boost_1_59_0.tar.bz2  
RUN tar -xf /tmp/boost_1_59_0.tar.bz2 -C /tmp/  
  
WORKDIR $BOOST_DIR  
  
# Compile Windows library  
RUN HOST=i686-w64-mingw32 && \  
echo "using gcc : $GCCVERSION : $HOST-g++ \  
: \  
<rc>$HOST-windres \  
<archiver>$HOST-ar \  
<cxxflags>-frandom-seed=boost1 \  
<ranlib>$HOST-ranlib \  
;" > user-config.jam && \  
./bootstrap.sh --without-icu  
  
RUN ./b2 toolset=gcc target-os=windows variant=release \  
threading=multi threadapi=win32 link=static \  
runtime-link=static --user-config=user-config.jam \  
\--without-mpi --without-python -sNO_BZIP2=1 \  
\--without-context --without-coroutine --without-coroutine2 \  
\--prefix=/usr/lib/boost stage  
  
RUN mv stage stage_windows  
  
# Compile Linux library  
RUN ./bootstrap.sh  
RUN ./b2 address-model=32 link=static \  
\--without-python --without-mpi \  
-sNO_BZIP2=1 stage  
  
RUN mv stage stage_linux  

