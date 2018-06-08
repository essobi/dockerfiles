FROM resin/rpi-raspbian:latest  
MAINTAINER Patrick Eichmann <phreakazoid@phreakazoid.com>  
  
RUN [ "cross-build-start" ]  
  
RUN apt-get update \  
&& apt-get install -y -q --no-install-recommends \  
mercurial \  
git \  
golang \  
wget \  
&& apt-get clean \  
&& rm -r /var/lib/apt/lists/*  
  
# Install Forego  
ENV GOPATH /opt/go  
ENV PATH $PATH:$GOPATH/bin  
RUN go get -u github.com/ddollar/forego  
  
ENV VERSION 0.7.3  
ENV DOWNLOAD_URL https://github.com/jwilder/docker-
gen/releases/download/$VERSION/docker-gen-linux-armhf-$VERSION.tar.gz  
ENV DOCKER_HOST unix:///tmp/docker.sock  
  
RUN wget -qO- $DOWNLOAD_URL | tar xvz -C /usr/local/bin  
  
RUN [ "cross-build-end" ]  
  
ENTRYPOINT ["/usr/local/bin/docker-gen"]  

