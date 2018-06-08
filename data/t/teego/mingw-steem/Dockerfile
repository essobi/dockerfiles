  
FROM teego/mingw-boost:1.60.0-Ubuntu-xenial  
  
MAINTAINER Aleksandr Zykov <tiger@mano.email>  
  
ENV BUILDBASE /r  
  
ENV BUILDROOT $BUILDBASE/build  
ENV MINGWROOT $BUILDBASE/mingw  
  
RUN ( \  
apt-get install -qy --no-install-recommends \  
cmake \  
python3 \  
doxygen \  
) &&\  
apt-get clean -qy  
  
ENV STEEM_VERSION 0.14.2  
ENV STEEM_RELEASE v$STEEM_VERSION  
  
RUN figlet "Steem" &&\  
mkdir -p $BUILDBASE/dist/steem-v$STEEM_VERSION-mingw64 &&\  
( \  
cd $BUILDROOT; \  
( \  
git clone https://github.com/steemit/steem.git steem-src &&\  
cd steem-src ;\  
( \  
git checkout $STEEM_RELEASE &&\  
git submodule update --init --recursive \  
) \  
) \  
) &&\  
( \  
cd $BUILDROOT; \  
( \  
mkdir -p steem-mingw &&\  
( \  
cd steem-mingw ;\  
( \  
cmake \  
-DLOW_MEMORY_NODE=ON \  
-DENABLE_CONTENT_PATCHING=OFF \  
-DFULL_STATIC_BUILD=ON \  
-DCMAKE_SYSTEM_NAME=Windows \  
-DCMAKE_C_COMPILER=x86_64-w64-mingw32-gcc \  
-DCMAKE_CXX_COMPILER=x86_64-w64-mingw32-g++ \  
-DCMAKE_RC_COMPILER=x86_64-w64-mingw32-windres \  
-DCMAKE_FIND_ROOT_PATH_MODE_PROGRAM=NEVER \  
-DCMAKE_FIND_ROOT_PATH_MODE_LIBRARY=ONLY \  
-DCMAKE_FIND_ROOT_PATH_MODE_INCLUDE=ONLY \  
-DCMAKE_BUILD_TYPE=RELEASE \  
-DCMAKE_FIND_ROOT_PATH=$MINGWROOT $BUILDROOT/steem-src \  
-DOPENSSL_ROOT_DIR=$MINGWROOT \  
-DBoost_USE_STATIC_LIBS=ON \  
-DBoost_THREADAPI=win32 \  
-DCMAKE_INSTALL_PREFIX=$BUILDBASE/dist/steem-v$STEEM_VERSION-mingw64 &&\  
make &&\  
make install \  
) \  
) \  
) \  
)  
  
RUN figlet "Package" &&\  
( \  
cd $BUILDBASE/dist; \  
(\  
zip -r $BUILDBASE/steem-v$STEEM_VERSION-mingw64.zip \  
steem-v$STEEM_VERSION-mingw64 \  
) \  
)  
  
RUN ( \  
cd $BUILDBASE; \  
(\  
sha256sum steem-v$STEEM_VERSION-mingw64.zip \  
) \  
)  
  
RUN figlet "Ready!"  

