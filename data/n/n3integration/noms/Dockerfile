FROM golang:1.7.3-alpine  
MAINTAINER n3integration@gmail.com  
  
VOLUME /data  
EXPOSE 8000  
RUN apk add git --update --no-cache && \  
go get -d -v github.com/attic-labs/noms/cmd/noms && \  
go install -v github.com/attic-labs/noms/cmd/noms && \  
rm -r /var/cache/apk && \  
rm -r /usr/share/man  
  
CMD ["noms", "serve", "/data"]  

