FROM alpine:edge as builder  
MAINTAINER tomas@aparicio.me  
  
ENV GOPATH /go  
ENV PATH /usr/local/go/bin:$PATH  
  
RUN mkdir /lib64 && ln -s /lib/libc.musl-x86_64.so.1 /lib64/ld-
linux-x86-64.so.2  
  
ADD . $GOPATH/src/github.com/h2non/imaginary  
  
RUN apk add --update \  
\--repository http://dl-cdn.alpinelinux.org/alpine/edge/testing \  
bash vips ca-certificates go gcc musl-dev fftw-dev vips-dev  
RUN go build -o bin/imaginary github.com/h2non/imaginary  
  
FROM alpine:edge  
RUN apk add --update --no-cache \  
\--repository http://dl-cdn.alpinelinux.org/alpine/edge/testing \  
bash vips ca-certificates  
COPY \--from=builder bin/imaginary bin/  
  
# Server port to listen  
ENV PORT 9000  
# Run the outyet command by default when the container starts.  
ENTRYPOINT ["bin/imaginary"]  
  
# Expose the server TCP port  
EXPOSE 9000  

