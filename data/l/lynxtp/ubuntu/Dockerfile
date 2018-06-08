FROM ubuntu:15.10  
MAINTAINER "Tom Vaughan <tvaughan@lynxtp.com>"  
RUN apt-get -q update \  
&& DEBIAN_FRONTEND=noninteractive \  
apt-get -q -y dist-upgrade \  
&& DEBIAN_FRONTEND=noninteractive \  
apt-get -q -y install \  
curl \  
make \  
software-properties-common=* \  
&& apt-get -q clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN curl -sL -o dumb-init.deb \  
https://github.com/Yelp/dumb-init/releases/download/v1.0.0/dumb-
init_1.0.0_amd64.deb \  
&& dpkg -i dumb-init.deb \  
&& rm -f dumb-init.deb  
  
# "--single-child" is required because of  
# https://github.com/Yelp/dumb-init/issues/51  
ENTRYPOINT ["dumb-init", "--single-child"]  
CMD []  

