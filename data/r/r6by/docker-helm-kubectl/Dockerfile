ARG HELM_VERSION=latest  
FROM dtzar/helm-kubectl:${HELM_VERSION} as helm  
  
FROM golang:alpine AS goget  
RUN apk --no-cache add git \  
&& go get github.com/mikefarah/yq \  
&& cp /go/bin/yq /tmp  
  
FROM alpine:3.7  
RUN apk add --no-cache curl ca-certificates jq pv  
COPY \--from=helm /bin/helm /usr/bin/  
COPY \--from=helm /usr/local/bin/kubectl /usr/bin/  
COPY \--from=goget /tmp/yq /usr/bin/  
  
CMD ["sh", "-c", "tail -f /dev/null"]  

