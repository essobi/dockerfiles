FROM alpine:3.7  
# Install interpreter languages and tools  
RUN apk add --no-cache \  
git \  
make \  
nodejs \  
nodejs-npm \  
python3 \  
ruby \  
&& python3 -m ensurepip \  
&& rm -r /usr/lib/python*/ensurepip \  
&& pip3 install --upgrade pip setuptools \  
&& rm -r /root/.cache \  
&& ln -s `which python3` /usr/bin/python  
  
# Install protobuf for each languages  
RUN apk add --no-cache \  
protobuf  
  
ENV GOPATH /go  
ENV PATH $GOPATH/bin:/node_modules/.bin/:$PATH  
  
RUN apk add --no-cache --virtual .builddeps \  
gcc \  
go \  
g++ \  
libstdc++ \  
make \  
python3-dev \  
ruby-dev \  
ruby-irb \  
ruby-rdoc \  
wget \  
&& go get -u github.com/golang/protobuf/protoc-gen-go \  
&& pip3 install \  
grpcio \  
grpcio-tools \  
&& npm install \  
google-protobuf \  
grpc-tools \  
&& wget -q -O /etc/apk/keys/sgerrand.rsa.pub
https://raw.githubusercontent.com/sgerrand/alpine-pkg-
glibc/master/sgerrand.rsa.pub \  
&& wget https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/2.27-r0/glibc-2.27-r0.apk \  
&& apk add glibc-2.27-r0.apk \  
&& gem install \  
grpc \  
grpc-tools \  
&& apk del .builddeps \  
&& rm /etc/apk/keys/sgerrand.rsa.pub glibc-2.27-r0.apk  
  
WORKDIR /defs  

