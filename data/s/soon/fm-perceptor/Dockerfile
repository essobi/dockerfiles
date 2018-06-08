FROM alpine:3.2  
RUN echo 'http://dl-4.alpinelinux.org/alpine/edge/main' >>
/etc/apk/repositories \  
&& apk update && apk add go git ca-certificates make && rm -rf
/var/cache/apk/* \  
&& wget -P /usr/local/bin http://public.thisissoon.com.s3.amazonaws.com/glide
\  
&& chmod +x /usr/local/bin/glide  
  
ENV GOPATH=/perceptor  
ENV GO15VENDOREXPERIMENT=1  
WORKDIR /perceptor/src/github.com/thisissoon/FM-Perceptor  
  
COPY ./glide.yaml /perceptor/src/github.com/thisissoon/FM-Perceptor/glide.yaml  
RUN glide up  
  
COPY . /perceptor/src/github.com/thisissoon/FM-Perceptor  
RUN make install && ln -s /perceptor/bin/perceptor /usr/local/bin/perceptor  
  
ENTRYPOINT perceptor  

