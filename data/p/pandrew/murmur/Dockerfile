FROM debian:jessie  
  
RUN apt-get update && apt-get -y install \  
curl \  
bzip2  
  
RUN curl -fL http://sourceforge.net/projects/mumble/files/Mumble/1.2.8/murmur-
static_x86-1.2.8.tar.bz2/download > /murmur.tar.bz2 \  
&& tar xvf /murmur.tar.bz2 \  
&& rm /murmur.tar.bz2  
  
EXPOSE 64738/tcp 64738/udp  
WORKDIR /murmur-static_x86-1.2.8  
  
ENTRYPOINT ["./murmur.x86", "-fg", "-ini", "murmur.ini"]  

