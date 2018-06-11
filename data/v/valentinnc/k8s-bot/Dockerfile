FROM golang:1.10.0-stretch  
WORKDIR /go/src/git.nautile.tech/Kubernetes/k8s-bot  
RUN go get -d -v github.com/tbruyelle/hipchat-go/hipchat  
COPY main.go .  
COPY global.go .  
COPY hipchat.go .  
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o k8s-bot .  
  
FROM alpine:latest  
ENV KUBE_LATEST_VERSION="v1.9.3"  
RUN apk update \  
&& apk --no-cache add ca-certificates bash curl \  
&& curl -L https://storage.googleapis.com/kubernetes-
release/release/${KUBE_LATEST_VERSION}/bin/linux/amd64/kubectl -o
/usr/local/bin/kubectl \  
&& chmod +x /usr/local/bin/kubectl  
  
WORKDIR /root/  
COPY \--from=0 /go/src/git.nautile.tech/Kubernetes/k8s-bot/k8s-bot .  
COPY docker-entrypoint.sh .  
CMD ["./docker-entrypoint.sh"]  

