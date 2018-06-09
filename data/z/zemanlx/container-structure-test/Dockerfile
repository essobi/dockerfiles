FROM golang:1.10.2-alpine3.7 AS builder  
  
RUN apk add --no-cache \  
gcc=6.4.0-r5 \  
git=2.15.0-r1 \  
make=4.2.1-r0 \  
musl-dev=1.1.18-r3 \  
&& go get github.com/golang/dep/cmd/dep  
  
# container-structure-test default version  
ARG CST_REF=v1.2.2  
ENV SOURCE_PATH=/go/src/github.com/GoogleContainerTools/container-structure-
test  
  
RUN git clone \  
\--depth 1 https://github.com/GoogleContainerTools/container-structure-
test.git \  
\--branch "$CST_REF" \  
"$SOURCE_PATH"  
  
WORKDIR $SOURCE_PATH  
# Download dependencies  
RUN dep ensure  
# Compile code  
RUN VERSION=$(git describe --tags || echo "$CST_REF-$(git describe --always)")
make \  
&& cp out/container-structure-test /  
  
# Distro image  
FROM alpine:3.7  
COPY \--from=builder /container-structure-test /bin/  
ENTRYPOINT ["/bin/container-structure-test"]  

