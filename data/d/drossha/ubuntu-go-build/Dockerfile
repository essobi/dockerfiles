FROM ubuntu  
  
RUN apt-get update && apt-get install -y \  
apt-utils \  
locales \  
wget \  
git \  
checkinstall \  
make \  
g++ \  
&& rm -rf /var/lib/apt/lists/* \  
&& localedef -i ru_RU -c -f UTF-8 -A /usr/share/locale/locale.alias
ru_RU.UTF-8  
ENV LANG ru_RU.utf8  
ENV GOPATH /tmp/build  
ENV GOROOT /usr/local/go/  
ENV PATH $PATH:/usr/local/go/bin  
  
RUN wget https://redirector.gvt1.com/edgedl/go/go1.9.2.linux-amd64.tar.gz \  
&& tar -C /usr/local -xzf go1.9.2.linux-amd64.tar.gz  
  
RUN mkdir /tmp/build  
  
RUN go get -u github.com/golang/dep/cmd/dep  
  
RUN wget https://github.com/google/protobuf/releases/download/v3.5.1/protobuf-
all-3.5.1.tar.gz \  
&& tar -xzf protobuf-all-3.5.1.tar.gz \  
&& cd protobuf-3.5.1 && ./configure \  
&& make && make install  
  
ENV LD_LIBRARY_PATH /usr/local/lib  
  
RUN go get -u google.golang.org/grpc  
  
RUN go get -u github.com/golang/protobuf/protoc-gen-go  
  
WORKDIR /tmp/build/src/github.com/golang/dep/cmd/dep  
  
RUN go build \  
&& cp dep /usr/local/bin  
  
ENV PATH $PATH:$GOPATH/bin  

