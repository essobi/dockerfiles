FROM debian:jessie-slim  
  
MAINTAINER Robert Schumann <gutmensch@n-os.org>  
  
ENV GRAPHITE_URL "graphite:2003"  
ENV GRAPHITE_PREFIX "room"  
ENV GIT_SSL_NO_VERIFY true  
ENV DEBIAN_FRONTEND noninteractive  
ENV PATH /opt:$PATH  
  
WORKDIR /opt  
  
COPY start.sh ./start.sh  
  
RUN set -x \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends wget git cmake build-essential
libhidapi-dev libusb-dev openssh-client \  
&& rm -rf /var/lib/apt/lists/* \  
&& git clone https://github.com/edorfaus/TEMPered.git \  
&& cd TEMPered \  
&& for i in 24 34 40 45 46; do \  
echo "adding pull request ${i}"; \  
wget -q --no-check-certificate
https://github.com/edorfaus/TEMPered/pull/$i.patch -O - | patch -p1; \  
done \  
&& make cmake \  
&& cd build \  
&& cmake -DCMAKE_INSTALL_PREFIX:PATH=/usr . \  
&& make \  
&& make install \  
&& cd /opt \  
&& rm -rf TEMPered \  
&& git clone https://github.com/s-leroux/TEMPer2.git \  
&& cd TEMPer2 \  
&& make \  
&& cp temper /usr/bin/ \  
&& cd /opt \  
&& rm -rf TEMPer2 \  
&& sed -i "s%GRAPHITE_URL%"$GRAPHITE_URL"%" start.sh \  
&& sed -i "s%GRAPHITE_PREFIX%"$GRAPHITE_PREFIX"%" start.sh \  
&& apt-get autoremove -y wget git cmake build-essential openssh-client \  
&& chmod +x start.sh  
  
CMD ["start.sh"]  

