FROM ubuntu:16.10  
MAINTAINER Nuno Agostinho <nunodanielagostinho@gmail.com>  
  
RUN apt-get update  
  
# Required to install Julia 0.5.2 while the newest version is not supported  
RUN apt-get install -y --no-install-recommends software-properties-common  
RUN add-apt-repository ppa:staticfloat/juliareleases  
RUN add-apt-repository ppa:staticfloat/julia-deps  
RUN apt-get update  
RUN apt-get install -y --no-install-recommends julia  
  
RUN apt-get install -y --no-install-recommends git  
RUN apt-get install -y --no-install-recommends ca-certificates  
RUN apt-get install -y --no-install-recommends curl  
RUN apt-get install -y --no-install-recommends hdf5-tools  
RUN apt-get install -y --no-install-recommends cmake  
RUN apt-get install -y --no-install-recommends unzip  
RUN apt-get install -y --no-install-recommends make  
RUN apt-get install -y --no-install-recommends gcc  
RUN apt-get install -y --no-install-recommends build-essential  
RUN apt-get install -y --no-install-recommends zlib1g zlib1g-dev  
  
ENV SW="/root/software"  
RUN mkdir -p ${SW}  
WORKDIR ${SW}  
  
ENV whippet="Whippet.jl"  
COPY ${whippet} ${whippet}  
WORKDIR ${whippet}  
  
RUN julia dependencies.jl  
  
WORKDIR ${SW}  
ENV PATH="${PATH}:${SW}/${whippet}/bin"

