FROM alpine:latest  
LABEL maintainer="Brian Glogower <xbglowx@gmail.com>"  
  
RUN apk --no-cache add ca-certificates bash curl git openssl wget && \  
update-ca-certificates && \  
git clone https://github.com/lukas2511/dehydrated.git  
  
WORKDIR /dehydrated  
ENTRYPOINT ["./dehydrated"]  
CMD ['-h']  

