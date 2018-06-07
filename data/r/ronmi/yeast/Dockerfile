# use debian stretch for http/2 support  
FROM ronmi/ynit-image:stretch  
MAINTAINER Ronmi Ren <ronmi@patrolavia.com>  
  
ENV YEASTVER v0.2.4  
ENV GOVER 1.7.4  
# install yeast  
RUN export deps="git wget ca-certificates" \  
&& export GOPATH="/gopath" \  
&& export GOROOT="/go" \  
&& export YEASTDIR="$GOPATH/src/github.com/Ronmi/yeast" \  
&& export YEASTLIB="/usr/local/share/yeast" \  
&& dpkg -l | awk '{print $2}' > /dpkg.orig \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends $deps \  
&& mkdir -p $GOPATH $GOROOT \  
&& wget -q -O - https://storage.googleapis.com/golang/go$GOVER.linux-
amd64.tar.gz | tar zxf - \  
&& mkdir -p $YEASTDIR $YEASTLIB \  
&& git clone -b $YEASTVER https://github.com/Ronmi/yeast $YEASTDIR \  
&& (cd $YEASTDIR && $GOROOT/bin/go get && $GOROOT/bin/go build && cp
$YEASTDIR/yeast /usr/local/bin/ && cp $YEASTDIR/index.html
$YEASTDIR/login.html $YEASTLIB/) \  
&& dpkg -l | awk '{print $2}' > /dpkg.new \  
&& diff -u0 dpkg.orig dpkg.new | grep '^\\+[a-z0-9]'|sed 's/+//' | xargs apt-
get purge -y --purge \  
&& apt-get autoremove --purge -y \  
&& apt-get clean \  
&& rm -fr /var/lib/apt/lists/* $GOPATH $GOROOT /dpkg.orig /dpkg.new  
  
# install nginx  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends nginx-light \  
&& ln -sf /etc/init.d/nginx /etc/ynit/ \  
&& apt-get clean \  
&& rm -fr /var/lib/apt/lists/*  
  
ADD yeast /etc/ynit/  
EXPOSE 80 8080  
VOLUME ["/var/lib/yeast", "/etc/nginx"]  

