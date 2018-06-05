# coq2scala  
#  
# VERSION 0.1.0  
FROM debian:latest  
MAINTAINER Shohei Yasutake <amutake.s@gmail.com>  
  
RUN apt-get update  
RUN apt-get upgrade -y  
RUN apt-get install -y build-essential git curl  
RUN curl -kL https://raw.github.com/hcarty/ocamlbrew/master/ocamlbrew-install
| env OCAMLBREW_BASE="/usr/local" OCAMLBREW_FLAGS="-o -n ." bash  
RUN git clone git://github.com/hemmi/coq2scala.git /opt/coq2scala  
WORKDIR /opt/coq2scala/coq-8.4pl2  
RUN ./configure -prefix /usr/local  
RUN make world  
RUN make install  
WORKDIR /  

