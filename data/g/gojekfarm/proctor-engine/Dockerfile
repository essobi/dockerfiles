FROM golang  
  
# Copy the local package files to the container's workspace.  
ADD . /go/src/github.com/gojekfarm/proctor-engine  
  
# Install glide  
RUN curl https://glide.sh/get | sh  
  
# Install dependency.  
RUN cd /go/src/github.com/gojekfarm/proctor-engine/ && glide install  
  
# Build binary.  
RUN go install github.com/gojekfarm/proctor-engine  
  
# Clean up.  
RUN rm -rf /go/src/github.com  
  
# Set app port  
ENV PROCTOR_APP_PORT 8080  
# Run the proctor-engine command by default when the container starts.  
ENTRYPOINT /go/bin/proctor-engine  
  
# Document that the service listens on port 8080.  
EXPOSE $PROCTOR_APP_PORT  
  

