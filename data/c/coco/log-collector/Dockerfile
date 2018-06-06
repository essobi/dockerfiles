FROM golang:1.8.3-alpine  
  
ENV PROJECT=log-collector  
COPY . /${PROJECT}-sources/  
  
RUN apk --no-cache --virtual .build-dependencies add git \  
&& ORG_PATH="github.com/Financial-Times" \  
&& REPO_PATH="${ORG_PATH}/${PROJECT}" \  
&& mkdir -p $GOPATH/src/${ORG_PATH} \  
&& ln -s /${PROJECT}-sources $GOPATH/src/${REPO_PATH} \  
&& cd $GOPATH/src/${REPO_PATH} \  
&& echo "Fetching dependencies..." \  
&& go get . \  
&& go build \  
&& mv ${PROJECT} /${PROJECT} \  
&& apk del .build-dependencies \  
&& rm -rf $GOPATH /var/cache/apk/*  
  
WORKDIR /  
  
CMD exec /log-collector -env=$ENV -workers=$WORKERS -buffer=$BUFFER
-batchsize=$BATCHSIZE -batchtimer=$BATCHTIMER -bucketName=$BUCKET_NAME
-awsRegion=$AWS_REGION  

