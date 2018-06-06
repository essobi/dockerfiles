FROM golang:1.7.1-wheezy  
  
# Copy the local package files to the container's workspace.  
ADD . /go/src/github.com/tleyden/cecil  
  
# Set our working dir to the cecil dir  
WORKDIR /go/src/github.com/tleyden/cecil  
  
# Note that running:  
# go install github.com/tleyden/cecil/...  
# Currently fails with errors:  
# goa/tool/cli/commands.go:454: too many arguments in call to c.CreateAccount  
# etc...  
#  
# And so in the meantime, just run:  
# go install github.com/tleyden/cecil  
#  
RUN go get -d -t github.com/tleyden/cecil/... && \  
go install github.com/tleyden/cecil  
  
ENTRYPOINT ["/go/bin/cecil"]  

