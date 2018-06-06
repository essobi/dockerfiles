FROM golang:1.9 as api  
WORKDIR /go/src/github.com/logicmonitor/k8s-chart-manager-controller  
RUN apt-get update  
RUN apt-get -y install bsdtar  
RUN go get github.com/golang/protobuf/protoc-gen-go  
RUN curl -L
https://github.com/google/protobuf/releases/download/v3.3.0/protoc-3.3.0-linux-x86_64.zip
| bsdtar -xf - --strip-components=1 -C /bin bin/protoc \  
&& chmod +x /bin/protoc  
COPY ./proto ./proto  
RUN mkdir api  
RUN protoc -I proto proto/api.proto \  
\--go_out=plugins=grpc:api  
  
FROM golang:1.9-alpine as codegen  
RUN apk add --update git  
RUN go get k8s.io/apimachinery/pkg/runtime  
RUN go get github.com/kubernetes/code-generator/cmd/deepcopy-gen || true \  
&& cd /go/src/github.com/kubernetes/code-generator \  
&& git checkout remotes/origin/release-1.8 \  
&& go get -d ./... \  
&& go install ./cmd/deepcopy-gen  
WORKDIR $GOPATH/src/github.com/logicmonitor/k8s-chart-manager-controller  
COPY ./ ./  
RUN deepcopy-gen \  
\--go-header-file="hack/boilerplate.go.txt" \  
\--input-dirs="github.com/logicmonitor/k8s-chart-manager-
controller/pkg/apis/v1alpha1" \  
\--bounding-dirs "github.com/logicmonitor/k8s-chart-manager-
controller/pkg/apis/v1alpha1" \  
\--output-file-base zz_generated.deepcopy  
  
FROM golang:1.9 as build  
WORKDIR $GOPATH/src/github.com/logicmonitor/k8s-chart-manager-controller  
COPY \--from=codegen $GOPATH/src/github.com/logicmonitor/k8s-chart-manager-
controller ./  
ARG VERSION  
RUN GOOS=linux GOARCH=amd64 CGO_ENABLED=0 go build -o /chart-manager-
controller -ldflags "-X \"github.com/logicmonitor/k8s-chart-manager-
controller/pkg/constants.Version=${VERSION}\""  
  
FROM golang:1.9 as test  
ARG CI  
ENV CI=$CI  
WORKDIR $GOPATH/src/github.com/logicmonitor/k8s-chart-manager-controller  
RUN go get -u github.com/alecthomas/gometalinter  
RUN gometalinter --install  
COPY \--from=build $GOPATH/src/github.com/logicmonitor/k8s-chart-manager-
controller ./  
RUN chmod +x ./scripts/test.sh; sync; ./scripts/test.sh  
RUN cp coverage.txt /coverage.txt  
  
FROM alpine:3.6  
LABEL maintainer="Jeff Wozniak <jeff.wozniak@logicmonitor.com>"  
RUN apk --update add ca-certificates \  
&& rm -rf /var/cache/apk/* \  
&& rm -rf /var/lib/apk/*  
WORKDIR /app  
COPY \--from=api /go/src/github.com/logicmonitor/k8s-chart-manager-
controller/api/* /tmp/  
COPY \--from=codegen /go/src/github.com/logicmonitor/k8s-chart-manager-
controller/pkg/apis/v1alpha1/zz_generated.deepcopy.go /tmp/  
COPY \--from=build /chart-manager-controller /bin  
COPY \--from=test /coverage.txt /coverage.txt  
  
ENTRYPOINT ["chart-manager-controller"]  
CMD ["manage"]  

