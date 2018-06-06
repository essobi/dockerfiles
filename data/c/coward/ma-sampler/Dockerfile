FROM ubuntu as base  
  
RUN apt-get update && \  
apt-get install -y software-properties-common  
  
RUN apt-add-repository -y ppa:jonathonf/ffmpeg-3 && \  
apt-get update && \  
apt-get install -y ffmpeg libavformat-dev libavresample-dev libswscale-dev  
  
FROM base as builder  
  
RUN apt-get update && \  
apt-get install -y curl git build-essential && \  
curl -O https://storage.googleapis.com/golang/go1.9.linux-amd64.tar.gz && \  
tar -xvf go1.9.linux-amd64.tar.gz && \  
mv go /usr/local && \  
export PATH="/usr/local/go/bin:$PATH"  
  
ENV GOPATH /go  
ENV PATH $GOPATH/bin:/usr/local/go/bin:$PATH  
  
RUN mkdir -p "$GOPATH/src" "$GOPATH/bin" && chmod -R 777 "$GOPATH"  
WORKDIR $GOPATH  
  
WORKDIR /go/src/github.com/dgmann/sampler  
COPY . .  
RUN go get -d -v ./... && CGO_ENABLED=1 GOOS=linux go build -a -installsuffix
cgo -o /sampler .  
  
FROM base  
  
WORKDIR /  
COPY \--from=builder /sampler /sampler  
  
ENV QUEUE_HOST=queue OUTPUT_QUEUE=images  
  
EXPOSE 1935  
ENTRYPOINT ["/sampler"]

