FROM ubuntu:14.04  
RUN apt-get update  
RUN apt-get install -y wget  
RUN apt-get install -y git  
RUN apt-get install -y build-essential  
RUN git clone https://github.com/google/protobuf  
RUN apt-get install -y curl  
RUN apt-get install -y unzip  
RUN apt-get install -y dh-autoreconf  
RUN cd protobuf && ./autogen.sh  
RUN cd protobuf && ./configure  
RUN cd protobuf && make  
RUN cd protobuf && make check  
RUN cd protobuf && make install  
RUN ldconfig  
RUN wget https://storage.googleapis.com/golang/go1.9.linux-amd64.tar.gz  
RUN tar -C /usr/local -xzf go1.9.linux-amd64.tar.gz  
RUN mkdir /wrap  
RUN mkdir /go/  
RUN mkdir /go/src  
RUN mkdir /go/bin  
RUN mkdir /go/pkg  
  
ENV PATH=$PATH:/usr/local/go/bin::/go/bin  
ENV GOPATH=/go  
  
RUN go get -u github.com/grpc-ecosystem/grpc-gateway/protoc-gen-grpc-gateway  
RUN go get -u github.com/grpc-ecosystem/grpc-gateway/protoc-gen-swagger  
RUN go get -u github.com/golang/protobuf/protoc-gen-go  
  
COPY data/wrap/*.go /wrap/  
  
COPY data/build_grpc.sh /build_grpc.sh  
COPY data/build_mw.sh /build_mw.sh  
COPY data/entrypoint.sh /entrypoint.sh  
  
RUN chmod +x /entrypoint.sh  
RUN chmod +x /build_grpc.sh  
RUN chmod +x /build_mw.sh  
  
VOLUME ["/develop/go", "/proto"]  
ENTRYPOINT ["/entrypoint.sh"]

