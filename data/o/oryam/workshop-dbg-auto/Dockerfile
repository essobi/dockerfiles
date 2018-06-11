FROM golang  
  
# Copy the local package files to the container's workspace.  
ADD . /go/src/github.com/ory-am/workshop-dbg  
  
# Build the outyet command inside the container.  
# (You may fetch or manage dependencies here,  
# either manually or with a tool like "godep".)  
RUN go install github.com/ory-am/workshop-dbg  
  
# Run the outyet command by default when the container starts.  
ENTRYPOINT /go/bin/workshop-dbg  
  
EXPOSE 5678

