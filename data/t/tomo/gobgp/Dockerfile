# gobgp (part of Ryu SDN Framework)  
#  
FROM golang  
  
MAINTAINER FUJITA Tomonori <fujita.tomonori@lab.ntt.co.jp>  
  
RUN apt-get update  
RUN apt-get install -qy --no-install-recommends wget lv tcpdump emacs24-nox  
  
ENV HOME /root  
WORKDIR /root  
  
RUN go get github.com/osrg/gobgp/gobgpd  
RUN go get github.com/osrg/gobgp/gobgp  
RUN ln -s /go/src/github.com/osrg/gobgp .  

