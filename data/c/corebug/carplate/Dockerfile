### BUILDER stage  
FROM golang:latest as builder  
  
RUN apt-get update  
  
RUN apt-get install -y \  
build-essential \  
cmake \  
curl \  
git \  
libcurl3-dev \  
libleptonica-dev \  
liblog4cplus-dev \  
libopencv-dev \  
libtesseract-dev \  
apt-utils \  
wget  
  
# Build OpenALPR from sources  
WORKDIR /srv  
RUN wget -O v2.3.0.tar.gz
https://github.com/openalpr/openalpr/archive/v2.3.0.tar.gz\  
&& tar -xvzf v2.3.0.tar.gz \  
&& mv /srv/openalpr-2.3.0 /srv/openalpr \  
&& mkdir /srv/openalpr/src/build  
  
WORKDIR /srv/openalpr/src/build  
RUN cmake -DCMAKE_INSTALL_PREFIX:PATH=/usr
-DCMAKE_INSTALL_SYSCONFDIR:PATH=/etc .. && \  
make -j2 && \  
make install  
  
# Now let's get protobuf  
RUN apt-get -y install protobuf-compiler libprotobuf-dev  
  
WORKDIR /go/src/github.com/corebug/carPlatesRecognition  
  
ENV CGO_ENABLED 1  
ADD recognitionClient/ ./recognitionClient  
ADD recognitionProtocol/ ./recognitionProtocol  
ADD recognitionServer/ ./recognitionServer  
  
RUN go get -u github.com/golang/protobuf/protoc-gen-go  
RUN go generate ./...  
RUN go get ./...  
RUN GOOS=linux go build -o server ./recognitionServer/main.go  
RUN GOOS=linux go build -o client ./recognitionClient/main.go  
  
### Actual image stage  
FROM bitnami/minideb:latest as recognitionServer  
RUN apt-get update && apt-get -y install openalpr  
WORKDIR /root/  
COPY \--from=builder /go/src/github.com/corebug/carPlatesRecognition/client
./client  
COPY \--from=builder /go/src/github.com/corebug/carPlatesRecognition/server
./server  
COPY \--from=builder
/go/src/github.com/corebug/carPlatesRecognition/recognitionServer/runtime_data
./runtime_data  
CMD ["./server"]  
EXPOSE 5000  
LABEL maintainer="Vitalii Turovets <vturov@softserveinc.com>"  

