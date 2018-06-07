# Start from a Debian image with the latest version of Go installed  
# and a workspace (GOPATH) configured at /go.  
FROM golang  
  
# Copy the local package files to the container's workspace.  
ADD . /go/src/ThisIsDisaster-API  
  
# Install revel and the revel CLI.  
RUN go get github.com/revel/revel  
RUN go get github.com/revel/cmd/revel  
RUN go get github.com/go-gorp/gorp  
RUN go get github.com/go-sql-driver/mysql  
  
# Use the revel CLI to start up our application.  
ENTRYPOINT revel run ThisIsDisaster-API dev 9000  
  
# Open up the port where the app is running.  
EXPOSE 9000  

