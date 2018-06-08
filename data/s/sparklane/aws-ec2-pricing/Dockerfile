# ### Build stage  
FROM golang:1.9.2 as builder  
WORKDIR /go/src/project  
ARG SSH_PRIVATE_KEY  
  
# Install glide  
ENV GLIDE_VERSION=v0.13.1  
RUN wget
https://github.com/Masterminds/glide/releases/download/$GLIDE_VERSION/glide-$GLIDE_VERSION-
linux-amd64.tar.gz \  
&& tar xvf glide-$GLIDE_VERSION-linux-amd64.tar.gz \  
&& cp linux-amd64/glide /go/bin/  
  
# Run glide  
COPY glide.* ./  
RUN glide install --skip-test  
  
# Install certificates for using SSL  
RUN apt-get install ca-certificates  
  
# Get sources and build app  
COPY *.go ./  
RUN ls /go/src  
#RUN go test -v -cover *.go  
RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -a -installsuffix cgo -o
app *.go  
  
# ### Run stage  
FROM scratch  
COPY \--from=builder /etc/ssl/ /etc/ssl/  
COPY \--from=builder /go/src/project/app /app  
ENTRYPOINT ["/app"]  

