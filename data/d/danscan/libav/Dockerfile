# Video Transcoding  
# Extends node base image  
FROM danscan/node  
  
# Add Universe & Multiverse Repositories  
RUN echo "deb http://us.archive.ubuntu.com/ubuntu/ precise multiverse"
>>/etc/apt/sources.list  
RUN echo "deb-src http://us.archive.ubuntu.com/ubuntu/ precise multiverse"
>>/etc/apt/sources.list  
RUN echo "deb http://us.archive.ubuntu.com/ubuntu/ precise-updates multiverse"
>>/etc/apt/sources.list  
RUN echo "deb-src http://us.archive.ubuntu.com/ubuntu/ precise-updates
multiverse" >>/etc/apt/sources.list  
RUN echo "deb http://us.archive.ubuntu.com/ubuntu/ precise universe"
>>/etc/apt/sources.list  
RUN echo "deb-src http://us.archive.ubuntu.com/ubuntu/ precise universe"
>>/etc/apt/sources.list  
RUN echo "deb http://us.archive.ubuntu.com/ubuntu/ precise-updates universe"
>>/etc/apt/sources.list  
RUN echo "deb-src http://us.archive.ubuntu.com/ubuntu/ precise-updates
universe" >>/etc/apt/sources.list  
RUN apt-get update  
  
# Install build deps  
RUN apt-get install -y build-essential pkg-config yasm libx264-dev libfaac-dev
libpng12-dev git  
  
# Clone Libav Latest  
RUN git clone git://git.libav.org/libav.git  
WORKDIR libav  
  
# Build Libav  
RUN ./configure --enable-gpl --enable-nonfree --enable-libx264 --enable-
libfaac  
RUN make  
RUN make install  
  
# Clean up  
WORKDIR ..  
RUN rm -r libav  
RUN apt-get remove -y build-essential yasm git

