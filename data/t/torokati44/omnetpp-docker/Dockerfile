FROM alpine:3.6  
MAINTAINER TÖRÖK Attila <torokati44@gmail.com>  
  
ENV PATH /opt/omnetpp-5.1.1/bin:$PATH  
RUN apk add --no-cache wget ca-certificates  
  
WORKDIR /opt  
RUN wget --progress=dot:giga https://bitbucket.org/torokati44/omnetpp-
docker/raw/c3074bba928e3679210af817a4b3e9203f7af1a1/omnetpp-5.1.1-src-core.tgz  
RUN tar xf omnetpp-5.1.1-src-core.tgz  
RUN rm omnetpp-5.1.1-src-core.tgz  
  
# for some reason clang doesn't work without the g++ package  
RUN apk add --no-cache make flex bison perl g++ clang binutils \  
libxml2-dev zlib git python3 py3-pip redis  
  
WORKDIR omnetpp-5.1.1  
RUN ./configure WITH_TKENV=no WITH_QTENV=no WITH_OSG=no WITH_OSGEARTH=no  
RUN make MODE=release  
  
RUN pip3 install --upgrade pip rq rq-dashboard flask flask_cors requests
patool shortuuid  
  
WORKDIR /opt  
RUN git clone https://torokati44@bitbucket.org/torokati44/doppy.git  
WORKDIR doppy  
  
RUN mkdir model_src model_bin results  

