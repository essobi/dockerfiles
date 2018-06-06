FROM debian:stretch-backports  
  
MAINTAINER Jérémy GIGNON <jeremy@gignon.fr>  
  
ENV GOROOT /usr/share/go  
ENV GOPATH /root/warpwallet_cracker  
ENV GOBIN $GOPATH/bin  
ENV PATH $GOPATH/bin:$GOROOT/bin:$PATH  
  
RUN apt-get update \  
&& apt-get upgrade -y \  
&& apt-get install -y git wget gnupg2 build-essential libssl-dev  
  
RUN cd /root \  
&& wget https://storage.googleapis.com/golang/go1.9.2.linux-amd64.tar.gz \  
&& tar -xvf go1.9.2.linux-amd64.tar.gz \  
&& mv go /usr/share  
  
RUN cd /root \  
&& git clone https://github.com/nachowski/warpwallet_cracker.git
warpwallet_cracker \  
&& cd warpwallet_cracker \  
&& go get ./... \  
&& go build warpwallet_cracker.go \  
&& chmod +x run.sh  

