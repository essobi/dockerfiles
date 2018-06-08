FROM micanzhang/golang-testing:1.9  
# build protoc  
ADD build-protoc.sh build-protoc.sh  
RUN /bin/sh build-protoc.sh && rm build-protoc.sh  
  
# golang protobuf plugin  
RUN go get -u github.com/golang/protobuf/protoc-gen-go  
  
# install glide  
RUN go get -u github.com/Masterminds/glide && rm -rf
$GOPATH/src/github.com/Masterminds/glide  
  
# install python3  
RUN apk add --no-cache python3 && \  
python3 -m ensurepip && \  
rm -r /usr/lib/python*/ensurepip && \  
pip3 install --upgrade pip setuptools && \  
if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \  
if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python;
fi && \  
rm -r /root/.cache  

