FROM gliderlabs/alpine:3.4  
ADD . /  
RUN apk --update add go git gcc linux-headers libc-dev \  
&& ORG_PATH="github.com/Financial-Times" \  
&& REPO_PATH="${ORG_PATH}/coco-fleet-unit-healthcheck" \  
&& export GOPATH=/gopath \  
&& mkdir -p $GOPATH/src/${ORG_PATH} \  
&& ln -s ${PWD} $GOPATH/src/${REPO_PATH} \  
&& cd $GOPATH/src/${REPO_PATH} \  
&& go get \  
&& go test \  
&& CGO_ENABLED=0 go build -a -installsuffix cgo -ldflags "-s" -o /coco-fleet-
unit-healthcheck ${REPO_PATH} \  
&& apk del go git gcc linux-headers libc-dev \  
&& rm -rf $GOPATH /var/cache/apk/*  
  
CMD exec /coco-fleet-unit-healthcheck \  
-fleetEndpoint=$FLEET_ENDPOINT \  
-socks-proxy=$SOCKS_PROXY \  
-timerBasedServices=$TIMER_BASED_SERVICES  

