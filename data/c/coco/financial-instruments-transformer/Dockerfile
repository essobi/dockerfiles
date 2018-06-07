FROM alpine:3.3  
ADD *.go /financial-instruments-transformer/  
  
RUN apk add --update bash \  
&& apk --update add git bzr \  
&& apk --update add go \  
&& export GOPATH=/gopath \  
&& REPO_PATH="github.com/Financial-Times/financial-instruments-transformer" \  
&& mkdir -p $GOPATH/src/${REPO_PATH} \  
&& mv financial-instruments-transformer/* $GOPATH/src/${REPO_PATH} \  
&& cd $GOPATH/src/${REPO_PATH} \  
&& go get -t ./... \  
&& go build \  
&& mv financial-instruments-transformer /financial-instruments-transformer-app
\  
&& apk del go git bzr \  
&& rm -rf $GOPATH /var/cache/apk/*  
  
CMD [ "/financial-instruments-transformer-app" ]  

