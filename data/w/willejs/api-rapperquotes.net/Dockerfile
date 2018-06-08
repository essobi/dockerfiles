# Start from a Debian image with the latest version of Go installed  
# and a workspace (GOPATH) configured at /go.  
FROM golang  
  
ENV HOST=0.0.0.0  
ENV PORT=8080  
# Go get and build  
RUN go get github.com/willejs/rapperquotes.com  
RUN go install github.com/willejs/rapperquotes.com  
  
# Run the service  
ENTRYPOINT /go/bin/rapperquotes.com  
  
# Document that the service listens on port 8080.  
EXPOSE 8080

