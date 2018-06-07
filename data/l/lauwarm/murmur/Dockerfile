FROM busybox:latest  
MAINTAINER lauwarm <lauwarm@mailbox.org>  
  
ENV version=1.3.0~2729~g2126495~snapshot  
  
ADD https://dl.mumble.info/murmur-static_x86-${version}.tar.bz2 /opt/  
  
RUN adduser -S murmur && \  
bzcat /opt/murmur-static_x86-${version}.tar.bz2 | tar -x -C /opt -f - && \  
rm /opt/murmur-static_x86-${version}.tar.bz2 && \  
mv /opt/murmur-static_x86-${version} /opt/murmur  
  
COPY murmur.ini /etc/murmur.ini  
  
EXPOSE 64738/tcp 64738/udp  
  
CMD ["/opt/murmur/murmur.x86", "-fg", "-v", "-ini", "/etc/murmur.ini"]  

