FROM ubuntu:16.10  
LABEL org.label-schema.schema-version="1.0" \  
org.label-schema.name="Dockerfile for Terraform development" \  
org.label-schema.description="This image provides a consistent Linux
development environment for Terraform development." \  
org.label-schema.url="https://github.com/hashicorp/terraform"  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
build-essential \  
git-core \  
less \  
vim \  
ca-certificates \  
curl \  
jq \  
unzip \  
zip \  
bash-completion \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV GOLANG_VERSION 1.8  
ENV GOLANG_DOWNLOAD_URL https://golang.org/dl/go$GOLANG_VERSION.linux-
amd64.tar.gz  
ENV GOLANG_DOWNLOAD_SHA256
53ab94104ee3923e228a2cb2116e5e462ad3ebaeea06ff04463479d7f12d27ca  
  
ENV GOPATH /go  
ENV PATH $GOPATH/bin:/usr/local/go/bin:$PATH  
  
RUN curl -fsSL "$GOLANG_DOWNLOAD_URL" -o golang.tar.gz \  
&& echo "$GOLANG_DOWNLOAD_SHA256 golang.tar.gz" | sha256sum -c - \  
&& tar -C /usr/local -xzf golang.tar.gz \  
&& rm golang.tar.gz \  
&& mkdir -p "$GOPATH/bin" "$GOPATH/pkg" "$GOPATH/src" \  
&& chmod -R 777 "$GOPATH" \  
&& go get -u -v \  
github.com/mitchellh/gox \  
github.com/kardianos/govendor \  
golang.org/x/tools/cmd/stringer \  
&& rm -fr "$GOPATH/src/github.com/mitchellh"
"$GOPATH/pkg/linux_amd64/github.com/mitchellh" \  
&& rm -fr "$GOPATH/src/github.com/kardianos"
"$GOPATH/pkg/linux_amd64/github.com/kardianos" \  
&& rm -fr "$GOPATH/src/golang.org/x/tools"
"$GOPATH/pkg/linux_amd64/golang.org/x/tools" \  
&& mv "$GOPATH/bin/gox" /usr/local/bin/ \  
&& mv "$GOPATH/bin/govendor" /usr/local/bin/ \  
&& mv "$GOPATH/bin/stringer" /usr/local/bin/  
  
VOLUME $GOPATH/src/github.com/hashicorp/terraform  
WORKDIR $GOPATH/src/github.com/hashicorp/terraform  

