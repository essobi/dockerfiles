FROM ubuntu:16.10  
MAINTAINER Nuno Agostinho <nunodanielagostinho@gmail.com>  
  
RUN apt-get update  
  
RUN apt-get install -y cmake  
RUN apt-get install -y libtbb-dev  
RUN apt-get install -y g++  
RUN apt-get install -y curl unzip  
RUN apt-get install -y zlib1g-dev  
RUN apt-get install -y libboost-all-dev  
RUN apt-get install -y autoconf  
  
ENV SW=/root/software/  
RUN mkdir -p ${SW}  
WORKDIR ${SW}  
  
ENV sailfish="sailfish"  
COPY ${sailfish} ${sailfish}  
WORKDIR "${SW}/${sailfish}/build"  
RUN cmake ..  
RUN make install  
ENV PATH="${PATH}:${SW}/${sailfish}/bin"  
ENV LD_LIBRARY_PATH="${LD_LIBRARY_PATH}:${SW}/${sailfish}/lib"  
WORKDIR ${SW}

