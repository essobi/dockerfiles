FROM ubuntu:14.04  
MAINTAINER Nobuyuki Kubota <nobu.k.jp@gmail.com>  
  
RUN apt-get update  
RUN apt-get install -y git ocaml omake ocaml-findlib camlp4-extra libounit-
ocaml-dev libextlib-ocaml-dev  
  
RUN git clone https://github.com/jubatus/jubatus.git  
WORKDIR jubatus/tools/jenerator  
  
RUN omake  
RUN omake install  

