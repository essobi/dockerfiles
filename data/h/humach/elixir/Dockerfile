FROM humach/erlang:19.3.4  
ENV ELIXIR_VERSION="1.4.4"  
ENV TAR_FILE="v${ELIXIR_VERSION}.tar.gz"  
ENV ELIXIR_DOWNLOAD_URL="https://github.com/elixir-
lang/elixir/archive/${TAR_FILE}"  
ENV BUILD_DEPS="autoconf gcc make musl-dev"  
ENV LANG="en_US.UTF-8"  
RUN set -ex \  
&& apk update \  
&& apk upgrade \  
&& apk add $BUILD_DEPS \--virtual .build-deps \  
&& wget $ELIXIR_DOWNLOAD_URL \  
&& tar xf $TAR_FILE \  
&& rm $TAR_FILE \  
&& cd elixir-$ELIXIR_VERSION \  
&& make -j $(grep -c ^processor /proc/cpuinfo) \  
&& make PREFIX=/usr install \  
&& cd .. \  
&& rm -r elixir-$ELIXIR_VERSION \  
&& apk del .build-deps \  
&& rm -f /var/cache/apk/*  
  
CMD ["iex"]  

