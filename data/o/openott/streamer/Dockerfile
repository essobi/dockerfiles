  
FROM ubuntu-debootstrap:14.04  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update -qqy  
RUN apt-get install -qqy cmake build-essential git unzip wget  
RUN apt-get install -qqy libboost-system-dev libboost-filesystem-dev libboost-
regex-dev libboost-thread-dev libboost-program-options-dev  
RUN apt-get install -qqy librados-dev  
  
RUN true \  
&& git clone https://github.com/theambient/spdlog.git /tmp/spdlog/ \  
&& cp -r /tmp/spdlog/include/spdlog /usr/local/include/ \  
&& rm -r /tmp/*  
  
RUN true \  
&& cd /tmp/ \  
&& wget -q https://s3.eu-central-1.amazonaws.com/theambient-
bottles/mongodriver.tar.gz \  
&& tar xzf mongodriver.tar.gz \  
&& cp -r mongodriver/* /usr/local/ \  
&& rm -r /tmp/*  
  
RUN true \  
&& cd /tmp \  
&& wget -q https://s3.eu-central-1.amazonaws.com/theambient-
bottles/bento4-1.4.2-Linux.deb \  
&& dpkg -i bento4-1.4.2-Linux.deb \  
&& rm -r /tmp/*  
  
RUN true \  
&& cd /tmp/ \  
&& wget -q https://s3.eu-central-1.amazonaws.com/theambient-
bottles/libav.tar.gz \  
&& tar xzf libav.tar.gz \  
&& cp -r libav-bin/* /usr/local/ \  
&& rm -r /tmp/*  
  
RUN apt-get install -qqy zlib1g-dev  
  
COPY . /src/  
  
RUN true \  
&& mkdir /tmp/build/ \  
&& cd /tmp/build/ \  
&& cmake /src/ \  
&& make \  
&& cp ./streamer /bin/ \  
&& rm -r /tmp/*  
  
ENTRYPOINT ["/bin/streamer"]  
  

