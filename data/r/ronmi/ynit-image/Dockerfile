FROM debian:oldstable  
MAINTAINER Ronmi Ren <ronmi@patrolavia.com>  
  
ENV YNITVER v0.1.3  
ENV GOVER 1.8.2  
RUN export deps="git wget ca-certificates" \  
&& export GOPATH="/gopath" \  
&& export GOROOT="/go" \  
&& export YNITDIR="$GOPATH/src/github.com/Ronmi/ynit" \  
&& dpkg -l | awk '{print $2}' > /dpkg.orig \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends $deps \  
&& mkdir -p $GOPATH $GOROOT \  
&& wget -q -O - https://storage.googleapis.com/golang/go$GOVER.linux-
amd64.tar.gz | tar zxf - \  
&& mkdir -p $YNITDIR \  
&& git clone -b $YNITVER https://github.com/Ronmi/ynit $YNITDIR \  
&& (cd $YNITDIR && $GOROOT/bin/go get && $GOROOT/bin/go build && cp
$YNITDIR/ynit /usr/local/bin/) \  
&& dpkg -l | awk '{print $2}' > /dpkg.new \  
&& diff -u0 dpkg.orig dpkg.new | grep '^\\+[a-z0-9]'|sed 's/+//' | xargs apt-
get purge -y --purge \  
&& apt-get autoremove --purge -y \  
&& apt-get clean \  
&& rm -fr /var/lib/apt/lists/* $GOPATH $GOROOT /dpkg.orig /dpkg.new  
  
# create default ynit directory  
RUN mkdir /etc/ynit  
  
CMD ["/usr/local/bin/ynit"]  

