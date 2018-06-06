FROM alpine  
  
ADD *.go /  
RUN apk add --update bash git alpine-sdk linux-headers go rsync \  
&& echo "http://dl-4.alpinelinux.org/alpine/edge/community" >>
/etc/apk/repositories \  
&& ORG_PATH="github.com/Financial-Times" \  
&& REPO_PATH="${ORG_PATH}/coco-neo4j-backup" \  
&& export GOPATH="/gopath" \  
&& mkdir -p $GOPATH/src/${ORG_PATH} \  
&& ln -nsf ${PWD} $GOPATH/src/${REPO_PATH} \  
&& cd $GOPATH/src/${REPO_PATH} \  
&& go get -v \  
&& go get -v -t \  
&& go test \  
&& go build ${REPO_PATH} \  
&& apk del go git alpine-sdk linux-headers \  
&& rm -rf $GOPATH /var/cache/apk/*  
  
CMD ["./coco-neo4j-backup"]  

