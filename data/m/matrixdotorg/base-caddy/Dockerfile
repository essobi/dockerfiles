FROM docker.io/matrixdotorg/base-alpine  
  
  
ENV GOPATH=/gopath  
  
ONBUILD ADD plugins.txt /plugins  
ONBUILD ARG BRANCH  
ONBUILD ARG CLONE_URL=github.com/mholt/caddy  
ONBUILD RUN apk upgrade --update \  
&& apk add --no-cache -t build-deps \  
build-base \  
libcap \  
go \  
git \  
&& mkdir -p ${GOPATH}/src/${CLONE_URL} \  
&& cd $GOPATH/src/${CLONE_URL} \  
&& git clone https://${CLONE_URL} . \  
&& git checkout ${BRANCH:-$(git describe --abbrev=0 --tags)} \  
&& cd caddy/caddymain \  
&& export LINE="$(grep -n "// This is where other plugins get plugged in
(imported)" < run.go | sed 's/^\\([0-9]\\+\\):.*$/\1/')" \  
&& head -n ${LINE} run.go > newrun.go \  
&& cat /plugins >> newrun.go \  
&& line=`expr ${LINE} \+ 1` \  
&& tail -n +${LINE} run.go >> newrun.go \  
&& rm -f run.go \  
&& mv newrun.go run.go \  
&& go get ${CLONE_URL}/... \  
&& mv $GOPATH/bin/caddy /usr/bin \  
&& setcap cap_net_bind_service=+ep /usr/bin/caddy \  
&& apk del --purge build-deps \  
&& rm -rf $GOPATH /plugins  

