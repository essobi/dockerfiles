# build stage  
FROM eduardoagrj/golang-dep AS builder  
ENV app golang-cep  
COPY Gopkg.* *.go /go/src/${app}/  
WORKDIR /go/src/${app}/  
RUN dep ensure --vendor-only \  
&& CGO_ENABLED=0 GOOS=linux go build -a -v -installsuffix netgo -installsuffix
cgo -o server *.go  
  
# final stage  
FROM scratch  
ENV app golang-cep  
WORKDIR /app  
COPY \--from=builder /go/src/${app}/ /app/  
EXPOSE 8080  
CMD [ "./server"]

