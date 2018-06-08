FROM golang  
MAINTAINER Rudolf Pliva rpliva@seznam.cz  
  
# install protobuf  
RUN apt-get update && apt-get install curl unzip -y  
RUN curl -OL
https://github.com/google/protobuf/releases/download/v3.0.0/protoc-3.0.0-linux-x86_64.zip
\  
&& unzip protoc-3.0.0-linux-x86_64.zip -d protoc3 \  
&& mv protoc3/bin/protoc /usr/bin/protoc  
  
# install letmegrpc  
RUN cd $GOPATH \  
&& mkdir -p ./src/github.com/gogo/letmegrpc \  
&& git clone https://github.com/gogo/letmegrpc ./src/github.com/gogo/letmegrpc
\  
&& git clone https://github.com/gogo/protobuf ./src/github.com/gogo/protobuf \  
&& go get google.golang.org/grpc \  
&& go get golang.org/x/net/context \  
&& (cd ./src/github.com/gogo/letmegrpc && make install)  
  
# install protoc-gen-gogo  
RUN go get github.com/gogo/protobuf/protoc-gen-gofast \  
&& go get github.com/gogo/protobuf/proto \  
&& go get github.com/gogo/protobuf/jsonpb \  
&& go get github.com/gogo/protobuf/protoc-gen-gogo \  
&& go get github.com/gogo/protobuf/gogoproto  
  
# copy proto files used in service  
ADD protos /var/letmegrpc/protos  
  
# share folder with protos  
VOLUME ["/var/letmegrpc/protos"]  
  
ENV PROTO_FILE "test.proto"  
ENV SERVICE_ADDRESS "localhost:12345"  
  
EXPOSE 8080  
  
CMD letmegrpc --addr=$SERVICE_ADDRESS --httpaddr=0.0.0.0:8080
\--proto_path=/var/letmegrpc/protos /var/letmegrpc/protos/$PROTO_FILE  

