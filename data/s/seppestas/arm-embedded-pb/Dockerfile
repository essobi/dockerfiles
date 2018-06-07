FROM productize/docker-arm-embedded:2017.10  
MAINTAINER Seppe Stas <seppe@productize.be>  
LABEL Description="Image for building embedded C projects using protobufs with
the gcc-arm-embedded toolchain"  
  
RUN apt-get update -qq && apt-get install -yq protobuf-compiler protobuf-c-
compiler python-protobuf && rm -rf /var/lib/apt/lists/*  

