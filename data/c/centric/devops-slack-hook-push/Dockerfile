FROM golang  
MAINTAINER William J Klos (bill.klos@centricconsulting.com)  
  
# Build the Spicoli server.  
RUN git clone https://github.com/centricconsulting/devops-slack-hook-push.git
/go/src/github.com/centricconsulting/devops-slack-hook-push  
RUN go get github.com/pborman/uuid  
RUN go get github.com/go-martini/martini  
RUN go get github.com/martini-contrib/binding  
RUN cd /go/src/github.com/centricconsulting/devops-slack-hook-push; go install  
  
# Start the Spicoli server.  
WORKDIR /go/src/github.com/centricconsulting/devops-slack-hook-push  
ENTRYPOINT ["devops-slack-hook-push"]  

