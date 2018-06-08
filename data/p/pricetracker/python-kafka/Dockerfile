FROM fulbito/fulbito-python3  
  
RUN apt-get update -y && apt-get install -y \  
librdkafka-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
ARG LIBRDKAFKA_NAME="librdkafka"  
ARG LIBRDKAFKA_VER="0.9.5"  
RUN wget -O "$BUILD_DIR/$LIBRDKAFKA_NAME.tar.gz"
"https://github.com/edenhill/librdkafka/archive/v$LIBRDKAFKA_VER.tar.gz" && \  
mkdir -p $BUILD_DIR/$LIBRDKAFKA_NAME-$LIBRDKAFKA_VER && \  
tar \  
\--extract \  
\--file "$BUILD_DIR/$LIBRDKAFKA_NAME.tar.gz" \  
\--directory "$BUILD_DIR/$LIBRDKAFKA_NAME-$LIBRDKAFKA_VER" \  
\--strip-components 1 && \  
cd "$BUILD_DIR/$LIBRDKAFKA_NAME-$LIBRDKAFKA_VER" && \  
./configure \  
\--prefix=/usr && \  
make -j "$(getconf _NPROCESSORS_ONLN)" && \  
make install  

