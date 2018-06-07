FROM debian:stable  
MAINTAINER Glenn Y. ROLLAND <glenn.rolland@netcat.io>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get install -q -y opam  
  
RUN apt-get install -q -y \  
mercurial darcs git m4 ocaml-nox pkg-config  
  
RUN opam init && \  
opam config setup -a  
  
RUN eval $(opam config env) && \  
opam switch 4.02.3  
  
RUN eval $(opam config env) && \  
opam install -y core base-bytes  
  
ADD . /usr/src/oconperf  
  
WORKDIR /usr/src/oconperf  
  
RUN eval $(opam config env) && \  
make clean && \  
make  
  
RUN cp /usr/src/oconperf/oconperf.native /usr/local/bin/oconperf  
RUN cp /usr/src/oconperf/scripts/run-server.sh /usr/local/bin/oconperf-server  
  
RUN rm -fr /usr/src/oconperf  
  
RUN apt-get autoremove -y  
  
EXPOSE 4217  
CMD /usr/local/bin/oconperf-server eth0  
  

