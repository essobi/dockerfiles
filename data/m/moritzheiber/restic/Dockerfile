FROM golang:alpine as builder  
  
ENV RESTIC_PATH="${GOPATH}/src/github.com/restic/restic"  
RUN apk --no-cache add git build-base && \  
git clone https://github.com/restic/restic "${RESTIC_PATH}" && \  
cd "${RESTIC_PATH}" && \  
make  
  
FROM moritzheiber/alpine-base  
LABEL maintainer="Moritz Heiber <hello@heiber.im>"  
  
COPY \--from=builder /go/src/github.com/restic/restic/restic /tmp/restic  
RUN apk --no-cache add openssh ca-certificates fuse && \  
install -m0755 -o root -g root /tmp/restic /usr/bin/restic && \  
rm -f /tmp/restic  
  
ENTRYPOINT ["/usr/bin/restic"]  

