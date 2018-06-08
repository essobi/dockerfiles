FROM busybox:latest  
MAINTAINER Fabien Culpo <fabien.culpo@gmail.com>  
  
ENV version=1.2.19  
RUN adduser -S murmur  
  
ADD https://github.com/mumble-voip/mumble/releases/download/${version}/murmur-
static_x86-${version}.tar.bz2 /opt/  
RUN bzcat /opt/murmur-static_x86-${version}.tar.bz2 | tar -x -C /opt -f - && \  
rm /opt/murmur-static_x86-${version}.tar.bz2 && \  
mv /opt/murmur-static_x86-${version} /opt/murmur  
  
# Copy in our slightly tweaked INI  
COPY murmur.ini /etc/murmur.ini  
  
# Forward appropriate ports  
EXPOSE 64738/tcp 64738/udp  
  
# Run murmur  
CMD ["/opt/murmur/murmur.x86", "-fg", "-v", "-ini", "/etc/murmur.ini"]  

