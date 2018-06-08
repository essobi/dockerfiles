FROM alpine:3.6  
RUN apk update && \  
apk upgrade && \  
apk add --nocache ca-certificates wget bash git openssh && \  
update-ca-certificates  
  
# https://stackoverflow.com/questions/34729748/installed-go-binary-not-found-
in-path-on-alpine-linux-docker  
RUN mkdir /lib64 && ln -s /lib/libc.musl-x86_64.so.1 /lib64/ld-
linux-x86-64.so.2  
  
ENV REVIEWDOG_VERSION 0.9.8  
RUN wget -O /usr/local/bin/reviewdog -q
https://github.com/haya14busa/reviewdog/releases/download/$REVIEWDOG_VERSION/reviewdog_linux_amd64
&& \  
chmod +x /usr/local/bin/reviewdog  
  
CMD ["/usr/local/bin/reviewdog"]  

