FROM textlab/ubuntu-essential  
MAINTAINER Joe Zhu <joe.zhu@bdi.ox.ac.uk>  
RUN apt-get update -qq \  
&& apt-get install -qq git build-essential autoconf autoconf-archive
libcppunit-dev zlib1g-dev \  
&& apt-cache policy zlib*  
RUN git clone \--recursive https://github.com/mcveanlab/DEploid.git  
WORKDIR /DEploid  
RUN ./bootstrap  
RUN make  
ENTRYPOINT ["./dEploid"]  
  

