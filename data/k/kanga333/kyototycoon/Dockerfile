FROM alpine  
  
ENV LANG ja_JP.UTF-8  
ENV KYOTOCABINET_VERSION 1.2.76  
ENV KYOTOTYCOON_VERSION 0.9.56  
  
RUN apk update && apk upgrade && \  
apk --no-cache add libstdc++ lua && \  
apk --no-cache add --virtual build-dependencies build-base zlib-dev curl lua-
dev && \  
curl -SLO
http://fallabs.com/kyotocabinet/pkg/kyotocabinet-${KYOTOCABINET_VERSION}.tar.gz
&& \  
tar xzvf kyotocabinet-${KYOTOCABINET_VERSION}.tar.gz && \  
cd kyotocabinet-${KYOTOCABINET_VERSION} && \  
./configure && \  
sed -i -e "s/CXXFLAGS =/CXXFLAGS = -std=c++98/" ./Makefile && \  
sed -i -e "s/CFLAGS =/CFLAGS = -std=c++98/" ./Makefile && \  
make && \  
make install && \  
cd / && \  
curl -SLO
http://fallabs.com/kyototycoon/pkg/kyototycoon-${KYOTOTYCOON_VERSION}.tar.gz
&& \  
tar xzvf kyototycoon-${KYOTOTYCOON_VERSION}.tar.gz && \  
cd kyototycoon-${KYOTOTYCOON_VERSION} && \  
./configure --with-kc=/usr/local --enable-lua && \  
sed -i -e "s/CXXFLAGS =/CXXFLAGS = -std=c++98/" ./Makefile && \  
sed -i -e "s/CFLAGS =/CFLAGS = -std=c++98/" ./Makefile && \  
sed -i -e "/^#include <kttimeddb.h>$/a #include <unistd.h>" ./ktdbext.h && \  
make && \  
make install && \  
apk del build-dependencies && \  
rm -rf \  
kyotocabinet-${KYOTOCABINET_VERSION} \  
kyotocabinet-${KYOTOCABINET_VERSION}.tar.gz \  
kyototycoon-${KYOTOTYCOON_VERSION} \  
kyototycoon-${KYOTOTYCOON_VERSION}.tar.gz  
  
EXPOSE 1978  
  
CMD ["/usr/local/bin/ktserver"]  

