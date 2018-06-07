FROM golang:latest  
MAINTAINER dusty.wilson@scjalliance.com  
  
VOLUME /data  
EXPOSE 8000  
ENV NOMS_VERSION_NEXT=1  
RUN go get -d -v github.com/attic-labs/noms/cmd/noms  
RUN go install -v github.com/attic-labs/noms/cmd/noms  
  
CMD ["noms", "serve", "/data"]  

