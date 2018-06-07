FROM ubuntu  
MAINTAINER daniel@dionix.at  
  
RUN apt-get update  
RUN apt-get install -y mencoder libav-tools x264 gpac mediainfo  
RUN echo "nolirc=yes" >> /etc/mplayer/mplayer.conf  
RUN apt-get install -y wget libexpat1-dev libslang2-dev libncurses-dev build-
essential  
RUN cd /tmp/ && \  
wget http://www.lbreyer.com/gpl/xml-coreutils-0.8.1.tar.gz && \  
tar xzf xml-coreutils-0.8.1.tar.gz && \  
cd xml-coreutils-0.8.1 && \  
./configure --prefix /usr/local && \  
make && \  
make install  
  
COPY encode.sh /usr/local/bin/encode.sh  
RUN chmod a+x /usr/local/bin/encode.sh  
  
ENV PRESET="slow"  
ENV BITRATE=2400  
ENV MAXBITRATE=4800  
ENV BUFFERSIZE=9600  
ENV MINKEYINT=48  
ENV KEYINT=48  
ENV PASS=1  
ENV PROFILE=main  
ENV LEVEL=5.2  
ENV LEVELS=""  
CMD encode.sh $LEVELS

