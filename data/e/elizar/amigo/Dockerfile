# Golang 1.7  
FROM golang:1.7  
# Prepare default application directory  
ENV APPDIR $GOPATH/src/github.com/elizar/amigo  
RUN mkdir -p $APPDIR  
COPY . $APPDIR  
  
# Expose 8080  
EXPOSE 8080  
# Setup work dir and build binary  
WORKDIR $APPDIR  
RUN go build amigo.go  
  
# Run the compiled binary  
ENTRYPOINT ./amigo  

