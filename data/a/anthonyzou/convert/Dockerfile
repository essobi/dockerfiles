FROM ubuntu  
  
RUN apt-get update; apt-get install g++ build-essential \  
make libreadline-dev libncurses5-dev python3 ca-certificates atomicparsley
libav-tools -y && \  
rm -rf /var/lib/apt/lists/*  
  
ADD id3ed-1.10.4.tar.gz /tmp  
ADD mp3gain-1_5_2_r2-src.tar.gz /tmp  
  
ADD https://yt-dl.org/downloads/latest/youtube-dl /usr/local/bin/youtube-dl  
RUN chmod a+rx /usr/local/bin/youtube-dl  
  
WORKDIR /tmp/id3ed-1.10.4  
RUN ./configure; make; make install;  
  
WORKDIR /tmp/mp3gain-1_5_2_r2-src  
RUN make; make install;  
  
RUN mv /usr/bin/python3 /usr/bin/python  
ENV LANG C.UTF-8  
ENV LC_ALL C.UTF-8  
ADD check /tmp  
WORKDIR /tmp/music  

