FROM golang:1.10  
  
ENV PB_VER 3.5.1  
ENV PB_URL
https://github.com/google/protobuf/releases/download/v${PB_VER}/protoc-${PB_VER}-linux-x86_64.zip  
ENV PACKAGES="unzip jq curl bash git make gettext-base"  
  
RUN apt-get update \  
&& apt-get -y install ${PACKAGES} \  
&& apt-get clean \  
\  
&& echo "-- Install protoc" \  
\  
&& mkdir -p /tmp/protoc \  
&& curl -L ${PB_URL} > /tmp/protoc/protoc.zip \  
&& cd /tmp/protoc \  
&& unzip protoc.zip \  
&& cp /tmp/protoc/bin/protoc /usr/local/bin \  
&& cp -R /tmp/protoc/include/* /usr/local/include \  
&& chmod go+rx /usr/local/bin/protoc \  
&& cd /tmp \  
&& rm -r /tmp/protoc \  
\  
&& set -x \  
&& echo "Install grpc things" \  
\  
&& go get google.golang.org/grpc \  
&& go get github.com/golang/protobuf/protoc-gen-go \  
\  
&& echo "Install protoc plugins" \  
\  
&& go get -u github.com/grpc-ecosystem/grpc-gateway/protoc-gen-grpc-gateway \  
&& go get -u github.com/grpc-ecosystem/grpc-gateway/protoc-gen-swagger \  
\  
&& echo "Install golang tools" \  
&& go get -u github.com/golang/dep/cmd/dep \  
&& go get -u github.com/golang/lint/golint \  
&& go get -u github.com/wadey/gocovmerge \  
&& go get -u github.com/axw/gocov/... \  
&& go get -u github.com/AlekSi/gocov-xml \  
&& go get -u github.com/tebeka/go2xunit \  
&& go get -u github.com/jteeuwen/go-bindata/... \  
&& go get -u -d github.com/mattes/migrate/cli github.com/go-sql-driver/mysql \  
&& go build -tags 'mysql' -o ${GOPATH}/bin/migrate
github.com/mattes/migrate/cli \  
&& go get -u github.com/nicksnyder/go-i18n/goi18n \  
&& go get -u github.com/go-swagger/go-swagger/cmd/swagger \  
\  
&& echo "Clean up golang tools sources" \  
&& rm -rf ${GOPATH}/src/github.com/golang/dep/cmd/dep \  
&& rm -rf ${GOPATH}/src/github.com/golang/lint/golint \  
&& rm -rf ${GOPATH}/src/github.com/wadey/gocovmerge \  
&& rm -rf ${GOPATH}/src/github.com/axw/gocov \  
&& rm -rf ${GOPATH}/src/github.com/AlekSi/gocov-xml \  
&& rm -rf ${GOPATH}/src/github.com/tebeka/go2xunit \  
&& rm -rf ${GOPATH}/src/github.com/jteeuwen/go-bindata \  
&& rm -rf ${GOPATH}/src/github.com/mattes/migrate/cli \  
&& rm -rf ${GOPATH}/src/github.com/go-sql-driver/mysql \  
&& rm -rf ${GOPATH}/src/github.com/mattes/migrate/cli \  
&& rm -rf ${GOPATH}/src/github.com/nicksnyder/go-i18n/goi18n \  
&& rm -rf ${GOPATH}/src/github.com/go-swagger/go-swagger/cmd/swagger \  
\  
&& echo "Install gogo protoc" \  
\  
&& go get -u github.com/gogo/protobuf/proto \  
&& go get -u github.com/gogo/protobuf/jsonpb \  
&& go get -u github.com/gogo/protobuf/protoc-gen-gogo \  
&& go get -u github.com/gogo/protobuf/protoc-gen-gogofast \  
&& go get -u github.com/gogo/protobuf/protoc-gen-gogofaster \  
&& go get -u github.com/gogo/protobuf/protoc-gen-gogoslick \  
&& go get -u github.com/gogo/protobuf/gogoproto \  
&& go get -u github.com/gogo/protobuf/protoc-gen-gofast \  
\  
&& echo "Install protoc plugins" \  
&& go get -u github.com/mwitkow/go-proto-validators/protoc-gen-govalidators \  
\  
&& echo "Install other dependencies" \  
&& (go get -u github.com/googleapis/googleapis || stat
${GOPATH}/src/github.com/googleapis/googleapis/google) \  
&& (go get -u github.com/grpc-ecosystem/grpc-gateway/third_party/googleapis ||
stat ${GOPATH}/src/github.com/grpc-ecosystem/grpc-
gateway/third_party/googleapis) \  
\  
&& echo "Clean up" \  
\  
&& rm -rf ${GOPATH}/bin/example* \  
&& rm -rf /var/lib/apt/lists/*

