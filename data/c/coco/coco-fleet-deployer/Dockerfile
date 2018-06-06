FROM alpine  
  
ADD . /  
RUN apk --update add go git gcc linux-headers libc-dev \  
&& ORG_PATH="github.com/Financial-Times" \  
&& REPO_PATH="${ORG_PATH}/coco-fleet-deployer" \  
&& export GOPATH=/gopath \  
&& mkdir -p $GOPATH/src/${ORG_PATH} \  
&& ln -s ${PWD} $GOPATH/src/${REPO_PATH} \  
&& cd $GOPATH/src/${REPO_PATH} \  
&& go get \  
&& go test \  
&& CGO_ENABLED=0 go build -a -installsuffix cgo -ldflags "-s" -o /coco-fleet-
deployer ${REPO_PATH} \  
&& apk del go git gcc linux-headers libc-dev \  
&& rm -rf $GOPATH /var/cache/apk/*  
  
CMD /coco-fleet-deployer -fleetEndpoint=$FLEET_ENDPOINT -rootURI=$ROOT_URI
-destroy=$DESTROY -isDebug=$IS_DEBUG -etcd-url=$ETCD_URL -health-url-
prefix=$HEALTH_URL_PREFIX -health-endpoint=$HEALTH_ENDPOINT -service-name-
prefix=$SERVICE_NAME_PREFIX -no-of-secs-to-sleep-before-
restart=$NO_OF_SECS_TO_SLEEP_BEFORE_RESTART  
  

