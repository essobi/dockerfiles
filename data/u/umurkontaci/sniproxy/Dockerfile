FROM debian  
RUN apt-get update  
  
RUN apt-get install -y \  
git \  
automake \  
build-essential \  
autotools-dev \  
cdbs \  
debhelper \  
dh-autoreconf \  
dpkg-dev \  
gettext \  
libev-dev \  
libpcre3-dev \  
libudns-dev \  
pkg-config \  
fakeroot \  
perl \  
curl  
  
RUN git clone https://github.com/dlundquist/sniproxy.git  
  
WORKDIR sniproxy  
  
RUN ./autogen.sh && ./configure && make install  
  
COPY proxy.conf /sniproxy/proxy.conf  
  
EXPOSE 80 443  
ENTRYPOINT ["sniproxy", "-f"]  
  
CMD ["-c", "/sniproxy/proxy.conf"]  

