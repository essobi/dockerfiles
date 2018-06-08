FROM alpine  
  
COPY entrypoint.sh /  
RUN apk add --no-cache \  
git \  
gcc \  
binutils \  
make \  
perl \  
mtools \  
musl-dev \  
xz-dev \  
&& mkdir /build \  
&& cd /build \  
&& git clone git://git.ipxe.org/ipxe.git \  
&& chmod +x /entrypoint.sh  
  
VOLUME ["/output"]  
WORKDIR /build/ipxe/src  
CMD ["/entrypoint.sh"]  

