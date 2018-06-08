FROM busybox:latest  
MAINTAINER SM  
  
ENV version=1.2.19  
# Download statically compiled murmur and install it to /opt/murmur  
ADD https://github.com/mumble-voip/mumble/releases/download/${version}/murmur-
static_x86-${version}.tar.bz2 /opt/  
RUN bzcat /opt/murmur-static_x86-${version}.tar.bz2 | tar -x -C /opt -f - && \  
rm /opt/murmur-static_x86-${version}.tar.bz2 && \  
mv /opt/murmur-static_x86-${version} /opt/murmur  
  
# Forward apporpriate ports  
EXPOSE 64738/tcp 64738/udp  
  
# Read murmur.ini and murmur.sqlite from /data/  
VOLUME ["/data"]  
  
# Run murmur  
ENTRYPOINT ["/opt/murmur/murmur.x86", "-fg", "-v"]  
CMD ["-ini", "/data/murmur.ini"]

