FROM alpine:edge  
LABEL maintainer="Jason Raimondi <jason@raimondi.us>"  
  
ENV GOPATH /go  
ENV PATH /usr/local/bin:$PATH  
  
RUN apk add --no-cache --update ca-certificates \  
&& apk add --no-cache --virtual .build-deps go gcc git libc-dev \  
&& go get github.com/ssimunic/gossm/cmd/gossm \  
&& go build github.com/ssimunic/gossm/cmd/gossm \  
&& mv gossm /usr/local/bin/ \  
&& mkdir -p /configs /var/log/gossm \  
&& apk del --purge .build-deps \  
&& rm -rf /var/cache/apk*  
  
ADD configs /configs  
  
CMD ["gossm", "-config", "/configs/default.json", "-http", ":8080", "-log",
"/var/log/gossm/gossm.log"]  
  
EXPOSE 8080  

