FROM golang:1.10.2-alpine3.7  
  
RUN apk --update add git  
RUN go get github.com/justincampbell/timeago && \  
go get k8s.io/api/core/v1 && \  
go get k8s.io/client-go/rest && \  
go get k8s.io/client-go/tools/clientcmd && \  
go get k8s.io/apimachinery/pkg/apis/meta/v1 && \  
go get github.com/dgrijalva/jwt-go && \  
go get github.com/labstack/echo  
  
WORKDIR /gopath/src/app  
COPY . /gopath/src/app/  
  
RUN go build -ldflags "-s -w" -o /opt/app/imageDashboard  
  
FROM alpine:3.7  
  
COPY \--from=0 /opt/app/imageDashboard /opt/app/  
COPY ./views /opt/app/views  
  
WORKDIR /opt/app/  
  
ENV PORT 3000  
CMD ["./imageDashboard"]  

