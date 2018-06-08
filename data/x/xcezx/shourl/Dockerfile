FROM golang:1.6-alpine  
  
RUN apk add --update-cache --no-cache --virtual build-dependencies git \  
&& go get github.com/xcezx/shourl \  
&& apk del build-dependencies  
  
EXPOSE 4800  
ENTRYPOINT ["shourl"]  
CMD ["-h"]  

