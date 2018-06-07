FROM golang:1.6  
MAINTAINER Seong-Min Kang <seong-min.kang@lendico.de>  
LABEL description="Heka built image for integrating custom plugins."  
  
WORKDIR /  
RUN apt-get update && apt-get install -y \  
cmake \  
debhelper \  
fakeroot \  
gcc \  
git \  
make \  
patch \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
  
&& git clone https://github.com/mozilla-services/heka  
  
RUN /bin/bash -c "cd /heka && source ./build.sh \  
&& make install \  
"  
  
ADD scripts/run-hekad.sh /run-hekad.sh  
CMD ["/run-hekad.sh"]  

