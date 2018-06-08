# ex: ts=4 sts=4 sw=4 et:  
  
FROM golang:1.7  
  
RUN apt-get update && \  
apt-get install -y curl build-essential && \  
curl -O https://capnproto.org/capnproto-c++-0.5.3.tar.gz && \  
tar zxf capnproto-c++-0.5.3.tar.gz && \  
cd capnproto-c++-0.5.3 && \  
./configure && \  
make check && \  
make install && \  
cd .. && \  
rm -rf capnproto-c++-0.5.3 && \  
apt-get remove -y curl build-essential  
RUN go get zombiezen.com/go/capnproto2/...  
  
COPY entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
  

