#FROM databoxsystems/base-image-ocaml:alpine-3.4_ocaml-4.04.2 as BUILDER  
FROM ocaml/opam:alpine-3.6_ocaml-4.04.2 as BUILDER  
  
WORKDIR /core-network  
ADD core-network.export core-network.export  
  
RUN sudo apk update && sudo apk add alpine-sdk bash gmp-dev perl autoconf
linux-headers &&\  
opam remote add git https://github.com/ocaml/opam-repository.git &&\  
opam pin add -n mirage-net-psock.0.1.0 https://github.com/sevenEng/mirage-net-
psock.git &&\  
opam switch import core-network.export  
  
ADD . .  
RUN sudo chown opam: -R . && opam config exec \-- jbuilder build
bin/core_network.exe  
  
FROM alpine:3.6  
WORKDIR /core-network  
ADD start.sh start.sh  
RUN apk update && apk add bash gmp-dev iptables iproute2 tcpdump  
COPY \--from=BUILDER /core-network/_build/default/bin/core_network.exe core-
network  
  
EXPOSE 8080  
LABEL databox.type="core-network"  
  
ENTRYPOINT ["./start.sh"]  

