FROM ubuntu:16.04  
MAINTAINER Nakano Masaki <namachan10777@gmail.com>  
  
RUN apt-get update  
RUN apt-get upgrade -qy  
RUN apt-get install -qy opam  
RUN apt-get install -qy m4  
RUN opam init --comp=4.05.0  
  
RUN opam install --yes jbuilder  
  
# opam path setting  
RUN echo "eval `opam config env`" > ~/.bashrc  
# cleaning apt cache  
RUN apt-get clean -qq -y && rm -rf /var/lib/apt/lists/*  
  
RUN mkdir /ci  
WORKDIR /ci  
  
ENTRYPOINT ["/bin/bash"]  

