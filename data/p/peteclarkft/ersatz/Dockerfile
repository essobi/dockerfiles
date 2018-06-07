FROM golang:1.9-alpine  
  
ENV PROJECT=ersatz  
COPY . /${PROJECT}-sources/  
  
RUN apk --no-cache --virtual .build-dependencies add git \  
&& ORG_PATH="github.com/peteclark-ft" \  
&& REPO_PATH="${ORG_PATH}/${PROJECT}" \  
&& mkdir -p $GOPATH/src/${ORG_PATH} \  
&& ln -s /${PROJECT}-sources $GOPATH/src/${REPO_PATH} \  
&& cd $GOPATH/src/${REPO_PATH} \  
&& go get -u github.com/kardianos/govendor \  
&& $GOPATH/bin/govendor sync \  
&& go build \  
&& mv ${PROJECT} /${PROJECT} \  
&& apk del .build-dependencies \  
&& rm -rf $GOPATH /var/cache/apk/*  
  
WORKDIR /  
  
CMD [ "/ersatz" ]  

