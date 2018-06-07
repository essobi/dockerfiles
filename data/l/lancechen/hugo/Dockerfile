FROM golang:1-alpine  
  
RUN apk update \  
&& apk add git \  
&& go get -v github.com/spf13/hugo \  
&& rm -rf /vaar/cache/apk/*  
  
WORKDIR /build  
ENTRYPOINT ["hugo"]  
CMD ["version"]  

