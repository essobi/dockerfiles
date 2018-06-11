# golang image where workspace (GOPATH) configured at /go.  
FROM golang  
  
# Install dependencies  
RUN go get github.com/gorilla/handlers  
RUN go get github.com/gorilla/mux  
RUN go get github.com/night-codes/mgo-ai  
RUN go get golang.org/x/crypto/bcrypt  
RUN go get gopkg.in/mgo.v2/bson  
  
# copy the local package files to the container workspace  
COPY . /go/src/2C_vehicle_ms  
  
# Build the users command inside the container.  
RUN go install 2C_vehicle_ms/cmd/app  
  
# Run the users microservice when the container starts.  
ENTRYPOINT /go/bin/app  
  
# Service listens on port 6005.  
EXPOSE 6005  

