# Operating system image:  
FROM ubuntu:16.04  
MAINTAINER Niene Boeijen <niene@webmapper.net>  
  
ENV BUILD_PACKAGES cmake wget git ca-certificates build-essential  
ENV DEP_PACKAGES libsqlite3-dev zlib1g-dev  
  
ENV DATA_DIR data_tiles  
  
# Create data directory  
RUN mkdir -p $DATA_DIR  
  
RUN apt-get -qq update && apt-get -qq --yes upgrade \  
&& apt-get install -y $BUILD_PACKAGES \--no-install-recommends  
  
### Tippecanoe!  
RUN apt-get -y install $DEP_PACKAGES \  
&& cd / \  
&& git clone https://github.com/mapbox/tippecanoe.git tippecanoe \  
&& cd tippecanoe \  
# && git checkout tags/$TIPPECANOE_RELEASE \  
&& cd /tippecanoe \  
&& make \  
&& make install \  
&& cd / \  
# && rm -rf tippecanoe \  
#Tippecanoe now requires features from the 2011 C++ standard.  
RUN add-apt-repository -y ppa:ubuntu-toolchain-r/test \  
apt-get update -y \  
apt-get install -y g++-5 \  
export CXX=g++-5  
  
###  
ENTRYPOINT ["tippecanoe"]  

