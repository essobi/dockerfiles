FROM avezila/go  
  
# install protobuf  
RUN mkdir -p /tmp/protoc && \  
curl -L
https://github.com/google/protobuf/releases/download/v3.3.0/protoc-3.3.0-linux-x86_64.zip
> /tmp/protoc/protoc.zip && \  
cd /tmp/protoc && \  
unzip protoc.zip && \  
cp /tmp/protoc/bin/protoc /usr/local/bin && \  
chmod go+rx /usr/local/bin/protoc && \  
cd /tmp && \  
rm -r /tmp/protoc  
  
# Get the source from GitHub  
RUN go get google.golang.org/grpc  
# Install protoc-gen-go  
RUN go get github.com/golang/protobuf/protoc-gen-go  
RUN go get github.com/gogo/protobuf/protoc-gen-gogo  
RUN go get github.com/gogo/protobuf/protoc-gen-gofast  
RUN go get github.com/gogo/protobuf/protoc-gen-gogofast  
RUN go get github.com/gogo/protobuf/protoc-gen-gogofaster  
RUN go get github.com/gogo/protobuf/protoc-gen-gogoslick  
RUN go get github.com/gogo/protobuf/proto  
RUN go get github.com/gogo/protobuf/jsonpb  
RUN go get github.com/gogo/protobuf/gogoproto  
RUN go get golang.org/x/tools/cmd/goimports  
RUN go get github.com/jackspirou/pimports  
  
RUN mkdir -p /grpc  
RUN dnf install nodejs -y  
RUN npm i -g protobufjs && echo | pbjs -  
WORKDIR /grpc  
CMD mkdir -p generated && /usr/local/bin/protoc
--go_out=plugins=grpc:./generated --java_out=./generated
--js_out=library=grpc,binary:./generated `find . | grep .*\\.proto$  
  

