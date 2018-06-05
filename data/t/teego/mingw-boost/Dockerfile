  
FROM teego/mingw-openssl:1.0.2h-Ubuntu-xenial  
  
MAINTAINER Aleksandr Zykov <tiger@mano.email>  
  
ENV BUILDBASE /r  
  
ENV BUILDROOT $BUILDBASE/build  
ENV MINGWROOT $BUILDBASE/mingw  
  
ENV BOOST_VERSION 1.60.0  
  
RUN figlet "Boost" &&\  
mkdir -p $BUILDROOT/boost-build &&\  
( \  
cd $BUILDROOT; \  
wget -O boost_`echo $BOOST_VERSION | sed 's/\./_/g'`.tar.gz \  
http://sourceforge.net/projects/boost/files/boost/$BOOST_VERSION/boost_`echo
$BOOST_VERSION | sed 's/\./_/g'`.tar.gz/download &&\  
tar xfz boost_`echo $BOOST_VERSION | sed 's/\./_/g'`.tar.gz &&\  
( \  
cd boost_`echo $BOOST_VERSION | sed 's/\./_/g'`; \  
( \  
( \  
echo "using gcc : mingw : x86_64-w64-mingw32-g++ ;" > user-config.jam \  
) &&\  
( \  
./bootstrap.sh \  
\--without-icu \  
\--prefix=$MINGWROOT \  
) &&\  
( \  
./b2 --user-config=user-config.jam \  
\--layout=tagged \  
toolset=gcc-mingw \  
target-os=windows \  
variant=release \  
link=static \  
threading=multi \  
threadapi=win32 \  
abi=ms \  
architecture=x86 \  
binary-format=pe \  
address-model=64 \  
-sNO_BZIP2=1 \  
\--build-dir=$BUILDROOT/boost-build \  
\--without-mpi \  
\--without-python \  
install ||\  
/bin/true\  
) \  
) \  
) \  
)  
  
RUN figlet "Ready!"  

