FROM ontouchstart/grs:base  
  
ENV GOLANG_VERSION 1.7  
ENV GOLANG_DOWNLOAD_URL https://golang.org/dl/go$GOLANG_VERSION.linux-
amd64.tar.gz  
ENV GOLANG_DOWNLOAD_SHA256
702ad90f705365227e902b42d91dd1a40e48ca7f67a2f4b2fd052aaa4295cd95  
  
RUN curl -fsSL "$GOLANG_DOWNLOAD_URL" -o golang.tar.gz \  
&& echo "$GOLANG_DOWNLOAD_SHA256 golang.tar.gz" | sha256sum -c - \  
&& tar -C /usr/local -xzf golang.tar.gz \  
&& rm golang.tar.gz  
  
ENV GOPATH /go  
RUN mkdir -p "$GOPATH/src" "$GOPATH/bin" && chmod -R 777 "$GOPATH"  
RUN curl -sSf https://static.rust-lang.org/rustup.sh | sh  
  
RUN curl -fsSL
https://swift.org/builds/swift-2.2.1-release/ubuntu1510/swift-2.2.1-RELEASE/swift-2.2.1-RELEASE-
ubuntu15.10.tar.gz \  
-o swift-2.2.1-RELEASE-ubuntu15.10.tar.gz  
RUN curl -fsSL
https://swift.org/builds/swift-2.2.1-release/ubuntu1510/swift-2.2.1-RELEASE/swift-2.2.1-RELEASE-
ubuntu15.10.tar.gz.sig \  
-o swift-2.2.1-RELEASE-ubuntu15.10.tar.gz.sig  
RUN gpg --recv-key 21A56D5F  
RUN gpg swift-2.2.1-RELEASE-ubuntu15.10.tar.gz.sig  
RUN tar -xzvf swift-2.2.1-RELEASE-ubuntu15.10.tar.gz  
RUN rm swift-2.2.1-RELEASE-ubuntu15.10.tar.gz swift-2.2.1-RELEASE-
ubuntu15.10.tar.gz.sig  
  
ENV SWIFTPATH /swift-2.2.1-RELEASE-ubuntu15.10/usr  
ENV HOME /home  
ENV GOPATH $HOME/go:/go  
ENV PATH $HOME/bin:$HOME/go/bin:/go/bin:/usr/local/go/bin:$SWIFTPATH/bin:$PATH  
  
RUN go version  
RUN rustc --version  
RUN swift -version  
  
WORKDIR /home  

