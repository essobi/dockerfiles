FROM debian:jessie  
  
MAINTAINER gizmoh1683  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get install -y \  
usbutils \  
libflac-dev \  
libfaad2 \  
libmad0 \  
libasound2-dev \  
libasound2 \  
libasound2-data \  
wget \  
git \  
build-essential libmad0-dev libvorbis-dev libvo-aacenc-dev libfaad-dev
libmpg123-dev  
  
#WORKDIR /opt  
#RUN git clone https://github.com/ralph-irving/squeezelite.git  
#WORKDIR squeezelite  
# RUN ./configure  
#RUN make  
RUN wget https://github.com/Hypfer/squeezelite-
downloads/raw/master/squeezelite-x86-64  
  
#COPY squeezelite/squeezelite /opt/  
#WORKDIR /opt  
RUN chmod a+x squeezelite-x86-64  
  
CMD /squeezelite-x86-64 -o $SOUNDDEVICE -s $SERVER -n $CLIENTNAME -m
$CLIENTMAC  

