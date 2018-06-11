#!/usr/bin/env docker  
FROM visanalyticskit/vakserver_base:latest  
MAINTAINER visanalyticskit@gmail.com  
  
ENV GOPATH /opt/go  
ENV GOROOT /usr/local/go  
ENV PATH $PATH:$GOPATH/bin:$GOROOT/bin  
ENV SGROOT /opt/sync_gateway  
ENV SYNC_CONFIG_FILE /opt/sync_gateway/conf/config.json  
  
RUN apt-get -q update && DEBIAN_FRONTEND=noninteractive && \  
apt-get autoclean && apt-get -qy autoremove && \  
apt-get install -y bc build-essential && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN wget -N -q https://storage.googleapis.com/golang/go1.6.linux-amd64.tar.gz
&& \  
mkdir -p $GOPATH && \  
tar -C /usr/local -xzf go1.6.linux-amd64.tar.gz && rm go1.6.linux-amd64.tar.gz  
  
RUN go get github.com/tools/godep && \  
go get github.com/nsf/gocode && \  
go get golang.org/x/tools/cmd/goimports && \  
go get github.com/golang/lint/golint && \  
go get github.com/rogpeppe/godef  
  
RUN cd /opt && \  
git clone https://github.com/couchbase/sync_gateway.git && \  
cd $SGROOT && \  
git checkout release/1.2.1 && \  
git submodule update --init --recursive && \  
./build.sh  
  
RUN mkdir -p $SGROOT/data && mkdir -p $SGROOT/conf  
COPY scripts/config.json $SYNC_CONFIG_FILE  
  
# add init script for runit  
COPY scripts/run /etc/service/sync_gateway/run  
RUN chmod +x /etc/service/sync_gateway/run  
  
CMD ["/sbin/my_init"]  
  
EXPOSE 4984 4985  
VOLUME "/opt/sync_gateway/conf"

