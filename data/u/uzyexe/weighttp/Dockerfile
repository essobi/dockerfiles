FROM debian:jessie  
  
ENV LIBEV_VERSION 4.22  
ENV WEIGHTTP_VERSION 0.4  
RUN apt-get update -qq && \  
apt-get install -qy curl build-essential python  
RUN mkdir /src  
  
# libev  
WORKDIR /src  
RUN curl http://dist.schmorp.de/libev/libev-${LIBEV_VERSION}.tar.gz | tar xzf
-  
RUN ln -s libev-${LIBEV_VERSION} libev  
WORKDIR /src/libev  
RUN ./configure --prefix=/usr  
RUN make install  
RUN ldconfig  
  
# weighttp  
WORKDIR /src  
RUN curl
https://codeload.github.com/lighttpd/weighttp/tar.gz/weighttp-${WEIGHTTP_VERSION}
| tar xzf -  
RUN ln -s weighttp-weighttp-${WEIGHTTP_VERSION} weighttp  
WORKDIR /src/weighttp  
RUN ./waf configure  
RUN ./waf build  
RUN ./waf install  
  
# Cleaning  
RUN apt-get --purge remove -y curl build-essential dh-autoreconf pkg-config &&
\  
apt-get clean all && \  
rm -rf /var/lib/apt/lists/*  
  
ENTRYPOINT ["/usr/local/bin/weighttp"]  
CMD ["-h"]  

