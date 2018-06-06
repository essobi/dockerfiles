# Use the official go docker image built on debian.  
FROM golang:1.4.2  
# Grab the source code and add it to the workspace.  
ADD . /go/src/sa_categorize_ms  
WORKDIR /go/src/sa_categorize_ms  
  
RUN go get -d  
# Install revel and the revel CLI.  
#RUN go get github.com/revel/revel  
#RUN go get github.com/revel/cmd/revel  
# Install project dependencies  
#RUN go get gopkg.in/mgo.v2  
# Use the revel CLI to start up our application.  
ENTRYPOINT revel run sa_categorize_ms prod 3001  
  
# Open up the port where the app is running.  
EXPOSE 3001  

