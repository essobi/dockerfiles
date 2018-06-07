FROM debian:stretch  
  
ENV VERSION 0.7.1  
RUN apt-get update && \  
apt-get install -y wget build-essential automake libglib2.0 gtk-doc-tools
gobject-introspection gettext libtool gnutls-dev libxml2-dev libgsasl7-dev &&
\  
rm -rf /var/lib/apt/lists/*  
  
WORKDIR /tmp  
RUN wget https://github.com/gobby/libinfinity/archive/${VERSION}.tar.gz && \  
tar xf ${VERSION}.tar.gz && \  
rm ${VERSION}.tar.gz && \  
mv libinfinity-$VERSION libinfinity  
  
WORKDIR /tmp/libinfinity  
RUN ./autogen.sh --prefix=/usr && make && make install  
WORKDIR /tmp  
RUN rm -rf libinfinity  
  
RUN addgroup --gid 1234 gobby && \  
adduser --disabled-password --disabled-login --gecos "" \--gid 1234 --uid 1234
gobby  
  
USER gobby  
WORKDIR /home/gobby  
  
ENTRYPOINT ["/usr/bin/infinoted-0.7"]  

