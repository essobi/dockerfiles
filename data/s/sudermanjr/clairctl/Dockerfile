# We need dind in order to run the docker commands used by clairctl  
FROM docker:stable-dind  
  
# Get the config for clairctl in place  
COPY ${PWD}/clairctl.yml /root/clairctl.yml  
  
# Get necessary apk packages  
RUN apk add --update=yes curl g++ go git  
  
# Install reg  
RUN mkdir /go  
ENV GOPATH=/go  
RUN go get github.com/jessfraz/reg  
RUN go build github.com/jessfraz/reg  
RUN ln -s $GOPATH/bin/reg /usr/bin/reg  
  
# Install clairctl  
RUN curl https://raw.githubusercontent.com/jgsqware/clairctl/master/install.sh
-o install.sh  
RUN sh install.sh  
  
# Change workdir to /root so that the config will get picked up  
WORKDIR /root

