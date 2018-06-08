  
FROM ubuntu-debootstrap:14.04  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update -qqy \  
&& apt-get install -qqy cmake build-essential git unzip wget \  
&& apt-get install -qqy libboost-system-dev libboost-filesystem-dev libboost-
program-options-dev  
  
RUN true \  
&& git clone https://github.com/gabime/spdlog.git /tmp/spdlog/ \  
&& cd /tmp/spdlog \  
&& git checkout 9603c2a20cc1f7356e9bcd250ba466a9c0842a6d \  
&& cp -r /tmp/spdlog/include/spdlog /usr/local/include/ \  
&& cd ~ \  
&& rm -rf /tmp/*  
  
RUN true \  
&& cd /tmp/ \  
&& wget -q https://s3.eu-central-1.amazonaws.com/theambient-
bottles/bitstream-1.0.tar.bz2 \  
&& tar xjf bitstream-1.0.tar.bz2 \  
&& cp -r bitstream-1.0 /usr/local/include/bitstream \  
&& rm -rf /tmp/*  
  
RUN true \  
&& cd /tmp \  
&& wget -q https://s3.eu-central-1.amazonaws.com/theambient-
bottles/bento4-1.4.2-Linux.deb \  
&& dpkg -i bento4-1.4.2-Linux.deb \  
&& rm -r /tmp/*  
  
RUN true \  
&& git clone https://github.com/m50d/h264bitstream.git /tmp/h264bitstream \  
&& cd /tmp/h264bitstream \  
&& make -f Makefile.unix \  
&& mkdir -p /usr/local/include/h264bs/ \  
&& cp *.h /usr/local/include/h264bs/ \  
&& cp *.a /usr/local/lib/  
  
COPY . /src/  
  
RUN true \  
&& mkdir /tmp/build/ \  
&& cd /tmp/build/ \  
&& cmake /src/ \  
&& make \  
&& cp ./segmenter /bin/ \  
&& rm -r /tmp/*  
  
ENTRYPOINT ["/bin/segmenter"]  

