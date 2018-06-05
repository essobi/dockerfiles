FROM multiarch/crossbuild  
  
RUN apt-get update \  
&& apt-get install -q -y pkg-config  
  
# Install GOLANG  
ENV GO_VERSION 1.8.3  
RUN curl -fsSL "https://storage.googleapis.com/golang/go${GO_VERSION}.linux-
amd64.tar.gz" \  
| tar -xzC /usr/local  
  
ENV PATH="/go/bin:/usr/local/go/bin:${PATH}" \  
GOPATH="/go"  
WORKDIR /go  
  
COPY scripts /scripts  
  
# set env vars  
ENV
PKG_CONFIG_PATH="/usr/lib/pkgconfig/:/usr/local/lib/pkgconfig/:/usr/local/lib/libgit2/lib/pkgconfig:/usr/local/lib/openssl/lib/pkgconfig:/usr/local/lib/libssh2"  
RUN /scripts/configure.sh  
  

