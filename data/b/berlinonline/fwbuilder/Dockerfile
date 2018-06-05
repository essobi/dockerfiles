FROM ubuntu:16.04 as builder  
RUN apt-get update && \  
apt install --no-install-recommends -y \  
git \  
pbuilder \  
equivs \  
autoconf \  
automake \  
devscripts \  
pkg-config && \  
rm -rf /var/cache/apt/*  
ADD . /build/source  
WORKDIR /build/source  
RUN mk-build-deps --install --remove --tool 'apt-get --no-install-recommends
-y'  
RUN ./autogen.sh && make && make install  
  
FROM ubuntu:16.04  
RUN apt-get update && \  
apt-get install -y \  
zlib1g \  
libqt4-designer libqt4-opengl libqt4-svg libqtgui4 libqtwebkit4 \  
libxml2 \  
libxslt1.1 \  
libssl1.0.0 \  
gnome-themes-standard \  
gnome-themes-ubuntu \  
light-themes \  
libsnmp-dev \  
openssh-client && \  
rm -rf /var/lib/apt/lists/*  
COPY \--from=builder /usr/local/bin/* /usr/local/bin/  
COPY \--from=builder /usr/local/share/fwbuilder*
/usr/local/share/fwbuilder-5.3.7/  
VOLUME ["/root/.config"]  
ENTRYPOINT ["/usr/local/bin/fwbuilder"]  
  

