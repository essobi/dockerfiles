FROM ubuntu:16.04  
MAINTAINER namachan10777 <namachan10777@gmail.com>  
  
RUN apt-get update  
RUN apt-get upgrade -qy  
RUN apt-get install -qy opam  
RUN apt-get install -qy m4  
RUN opam init --comp=4.06.0  
  
RUN opam install --yes jbuilder  
RUN opam install --yes menhir sedlex  
RUN opam install --yes ppx_inline_test  
RUN opam install --yes core  
RUN opam install --yes yojson  
RUN opam install --yes ppx_deriving_yojson  
  
# opam path setting  
RUN echo "eval `opam config env`" > ~/.bashrc  
# cleaning apt cache  
RUN apt-get clean -qq -y && rm -rf /var/lib/apt/lists/*  
  
RUN mkdir /ci  
WORKDIR /ci  
  
ENTRYPOINT ["/bin/bash"]  

