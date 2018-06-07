FROM debian:jessie  
LABEL maintainer "Tom Barlow <tom.barlow@docker.com>"  
  
RUN dpkg --add-architecture i386 && \  
apt-get update && \  
apt-get install -y --no-install-recommends \  
libsdl-image1.2:i386 \  
libsdl-ttf2.0-0:i386 \  
libgtk2.0-0:i386 \  
libjpeg62-turbo:i386 \  
libglu1-mesa:i386 \  
libstdc++-4.9-dev \  
ca-certificates \  
bzip2 \  
wget && \  
apt-get autoremove -y && \  
apt-get clean -y  
  
# Install df  
RUN wget -O df.tar.bz2
http://www.bay12games.com/dwarves/df_40_24_linux.tar.bz2 && \  
tar xvf df.tar.bz2 && \  
rm df.tar.bz2  
  
WORKDIR /df_linux  
VOLUME /df_linux/data/save  
  
# Install dfhack  
RUN wget -O dfhack.tar.bz2
https://github.com/DFHack/dfhack/releases/download/0.40.24-r3/dfhack-0.40.24-r3-Linux-
gcc-4.9.2.tar.bz2 && \  
tar xvf dfhack.tar.bz2 && \  
rm -f dfhack.tar.bz2 && \  
mv /usr/lib/gcc/x86_64-linux-gnu/4.9/libstdc++.so libs/libstdc++.so.6  
  
CMD ["./df"]  

