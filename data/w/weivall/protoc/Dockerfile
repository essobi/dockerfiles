FROM golang  
  
RUN apt update && apt install -y unzip clang-format-3.5 && \  
wget
https://github.com/google/protobuf/releases/download/v3.2.0/protoc-3.2.0-linux-x86_64.zip
&& \  
unzip protoc-3.2.0-linux-x86_64.zip && \  
rm -rf protoc-3.2.0-linux-x86_64.zip && \  
mv /usr/bin/clang-format-3.5 /usr/bin/clang-format  
  
RUN go get -u github.com/golang/protobuf/proto && \  
go get -u github.com/golang/protobuf/protoc-gen-go  

