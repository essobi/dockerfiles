# Moby  
# ## .  
# ## ## ## ==  
# ## ## ## ## ## ===  
# /"""""""""""""""""\\___/ ===  
# ~~~ {~~ ~~~~ ~~~ ~~~~ ~~~ ~ / ===- ~~~  
# \\______ o __/  
# \ \ __/  
# \\____\\_______/  
#  
# docker run --rm -v $(pwd):/app -v /var/run/docker.sock:/var/run/docker.sock
pottava/moby build linuxkit.yml  
# docker run --rm -v $(pwd):/app -it pottava/moby run linuxkit  
  
FROM alpine:3.5  
  
# Commit at Apr 18, 2017, 18:31 PM UTC  
ENV MOBY_VERSION=f2d6752751318477ec86e4677514d5a4890249c1  
  
RUN apk --no-cache add \--virtual build-dependencies bash gcc musl-dev openssl
go git \  
  
# Install go 1.8  
&& export GOPATH=/go \  
&& mkdir -p /go/src \  
&& cd /go/src \  
&& GOLANG_VERSION=1.8.1 \  
&& GOLANG_SRC_URL=https://golang.org/dl/go$GOLANG_VERSION.src.tar.gz \  
&&
GOLANG_SRC_SHA256=33daf4c03f86120fdfdc66bddf6bfff4661c7ca11c5da473e537f4d69b470e57
\  
&& export GOROOT_BOOTSTRAP="$(go env GOROOT)" \  
&& wget -q "$GOLANG_SRC_URL" -O golang.tar.gz \  
&& echo "$GOLANG_SRC_SHA256 golang.tar.gz" | sha256sum -c \- \  
&& tar -C /usr/local -xzf golang.tar.gz \  
&& wget -q https://raw.githubusercontent.com/docker-
library/golang/master/1.8/alpine/no-pic.patch \  
&& cd /usr/local/go/src \  
&& patch -p2 -i /go/src/no-pic.patch \  
&& ./make.bash \  
&& chmod -R 777 /go \  
  
# Compile moby  
&& go get -u github.com/linuxkit/linuxkit/src/cmd/moby \  
&& cd /go/src/github.com/linuxkit/linuxkit \  
&& git checkout ${MOBY_VERSION} \  
&& go install github.com/linuxkit/linuxkit/src/cmd/moby \  
&& mv /go/bin/moby /usr/bin \  
  
&& apk del --purge -r build-dependencies \  
&& rm -rf /usr/local/go /usr/lib/go /go /var/cache/* /var/lib/apk*  
  
RUN apk --no-cache add tini docker qemu-system-x86_64  
  
WORKDIR /app  
  
ENTRYPOINT ["/sbin/tini", "--", "moby"]  
CMD ["--help"]  

