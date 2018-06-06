FROM ruby:2.3-alpine  
  
ENV PACKAGES "bash curl openssh-client file git openssl ca-certificates wget
libc6-compat build-base libffi-dev zip"  
RUN apk add --update $PACKAGES && rm -rf /var/cache/apk/*  
  
RUN curl -L 'https://github.com/stedolan/jq/releases/download/jq-1.5/jq-
linux64' -o /usr/local/bin/jq && chmod +x /usr/local/bin/jq  
  
RUN curl -L 'https://storage.googleapis.com/golang/go1.8.3.linux-amd64.tar.gz'
-o go.tar.gz && tar -C /usr/local -xzf go.tar.gz && rm -f go.tar.gz && mkdir
/lib64 && ln -s /lib/libc.musl-x86_64.so.1 /lib64/ld-linux-x86-64.so.2  
  
RUN mkdir -p /gopath/bin  
ENV GOPATH /gopath  
ENV GOBIN /gopath/bin  
ENV PATH $PATH:/usr/local/go/bin:$GOPATH/bin  

