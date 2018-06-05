FROM avezila/fedora  
  
ENV GOLANG_VERSION 1.9rc1  
ENV GOLANG_DOWNLOAD_URL
https://storage.googleapis.com/golang/go$GOLANG_VERSION.linux-amd64.tar.gz  
ENV GOLANG_DOWNLOAD_SHA256
a8ea2ac09878b7a5ac04fe52f144cdc64ab637230638af6975c0f1facbba3ec2  
  
RUN curl -fsSL "$GOLANG_DOWNLOAD_URL" -o golang.tar.gz \  
&& echo "$GOLANG_DOWNLOAD_SHA256 golang.tar.gz" | sha256sum -c - \  
&& tar -C /usr/local -xzf golang.tar.gz \  
&& rm golang.tar.gz  
  
ENV GOPATH /go  
ENV PATH $GOPATH/bin:/usr/local/go/bin:$PATH  
  
RUN mkdir -p "$GOPATH/src" "$GOPATH/bin" && chmod -R 777 "$GOPATH"  
WORKDIR $GOPATH  
  
COPY go-wrapper /usr/local/bin/  

