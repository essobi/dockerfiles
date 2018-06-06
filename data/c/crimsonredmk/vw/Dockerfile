FROM ubuntu:16.04  
ARG VERSION=8.5.0  
RUN apt-get update && apt-get install -y clang curl libtool zlib1g-dev m4
autoconf automake make libboost-program-options-dev && mkdir /app && cd /app
&& curl https://codeload.github.com/JohnLangford/vowpal_wabbit/tar.gz/$VERSION
-o vw.tar.gz && tar xzf vw.tar.gz && cd vowpal_wabbit-$VERSION && ./autogen.sh
&& make CXX='clang++ -static' test install && cd / && rm -rf /app && apt-get
autoremove --purge -y clang curl libtool zlib1g-dev m4 autoconf automake make
&& apt-get clean autoclean && rm -rf /var/lib/apt /var/lib/dpkg /var/lib/cache
/var/lib/log && mkdir /data  
  
EXPOSE 26542  
ENTRYPOINT ["/usr/local/bin/vw"]  
CMD ["--help"]  

