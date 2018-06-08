FROM alpine:3.4  
  
ENV PATH /go/bin:/usr/local/go/bin:$PATH  
ENV GOPATH /go  
ENV USER root  
  
RUN apk --update add \  
go \  
git \  
gcc \  
libc-dev \  
libltdl \  
libtool \  
libgcc \  
python \  
py-pip \  
jq \  
curl \  
wget \  
bash &&\  
pip install --upgrade awscli &&\  
mkdir /root/.aws && \  
go get -u github.com/cloudflare/cfssl/cmd/...  
  
COPY generator /generator  
  
# Expose volume for adding credentials  
VOLUME ["/root/.aws"]  
  
ENTRYPOINT /generator  

