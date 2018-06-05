FROM golang:1.9 as buildstage  
  
ENV GOPATH /go  
WORKDIR /go  
RUN go get -u github.com/golang/dep/cmd/dep  
RUN go get -d github.com/osrg/gobgp/gobgp  
RUN go get -d github.com/osrg/gobgp/gobgpd  
RUN cd /go/src/github.com/osrg/gobgp && dep ensure  
RUN go get github.com/osrg/gobgp/gobgp  
RUN go get github.com/osrg/gobgp/gobgpd  
  
FROM ubuntu:latest as runstage  
  
COPY \--from=buildstage /go/bin/gobgp /usr/bin  
COPY \--from=buildstage /go/bin/gobgpd /usr/bin  
  
RUN apt-get update -y  
RUN apt-get install -y \  
arping \  
curl \  
htop \  
iftop \  
iperf \  
iperf3 \  
iproute2 \  
iptables \  
iputils-ping \  
keepalived \  
ldnsutils \  
mtr \  
net-tools \  
openssh-client \  
python \  
socat \  
strace \  
tcpdump \  
vim  
  
CMD [ "bash" ]  

