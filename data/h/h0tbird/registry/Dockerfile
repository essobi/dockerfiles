#------------------------------------------------------------------------------  
# Set the base image for subsequent instructions:  
#------------------------------------------------------------------------------  
FROM alpine:3.4  
MAINTAINER Marc Villacorta Morera <marc.villacorta@gmail.com>  
  
#------------------------------------------------------------------------------  
# Environment variables:  
#------------------------------------------------------------------------------  
ENV GOPATH=/go \  
VERSION="2.4.1"  
#------------------------------------------------------------------------------  
# Install:  
#------------------------------------------------------------------------------  
RUN apk add --no-cache --update -t deps go git make \  
&& apk add --no-cache --update bash openssl ca-certificates \  
&& go get github.com/docker/distribution \  
&& cd ${GOPATH}/src/github.com/docker/distribution \  
&& git checkout tags/v${VERSION} -b ${VERSION} \  
&& make PREFIX=/usr clean binaries && mkdir /var/lib/registry \  
&& apk del --purge deps && rm -rf /go /tmp/* /var/cache/apk/*  
  
#------------------------------------------------------------------------------  
# Populate root file system:  
#------------------------------------------------------------------------------  
ADD rootfs /  
  
#------------------------------------------------------------------------------  
# Expose ports and entrypoint:  
#------------------------------------------------------------------------------  
EXPOSE 5000  
ENTRYPOINT ["/init"]  

