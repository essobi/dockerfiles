FROM golang:1.9-alpine  
  
RUN apk add --no-cache git \  
&& go get -v github.com/spf13/hugo \  
&& /go/bin/hugo new site /go/src/site  
  
WORKDIR /go/src/site  
  
COPY config.toml /go/src/site/config.toml  
COPY post/ /go/src/site/content/post/  
  
RUN git clone https://github.com/diwao/hestia-pure.git themes/hestia-pure  
  
EXPOSE 80  
COPY entrypoint.sh /go/entrypoint.sh  
  
Entrypoint ["/bin/ash", "/go/entrypoint.sh"]  

