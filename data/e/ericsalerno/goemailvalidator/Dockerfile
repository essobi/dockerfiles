FROM golang:1.9-alpine  
# Copy local package to the containers workspace  
ADD . /go/src/github.com/ericsalerno/goemailvalidator  
# Build package in container  
RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -a -tags netgo -ldflags '-w
-extldflags "-static"' github.com/ericsalerno/goemailvalidator  
  
FROM alpine  
COPY \--from=0 /go/goemailvalidator /goemailvalidator  
# Download blacklist.conf file  
ADD https://raw.githubusercontent.com/martenson/disposable-email-
domains/master/disposable_email_blacklist.conf /blacklist.conf  
  
# Set container entrypoint to compiled binary  
ENTRYPOINT /goemailvalidator  
  
# Expose port 8081  
EXPOSE 8081  

