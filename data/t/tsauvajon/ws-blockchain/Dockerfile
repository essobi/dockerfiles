### Client  
# Latest LTS  
FROM node as client  
  
# Copy the local package files to the container's workspace.  
COPY . /usr/src/app  
WORKDIR /usr/src/app/client  
  
# Build the client  
RUN yarn  
RUN yarn build  
  
### Server  
# Debian image with the latest version of Go installed  
FROM golang as server  
  
# Copy the local package files to the container's workspace.  
WORKDIR /go/src/github.com/tsauvajon/ws-blockchain/server  
COPY \--from=client /usr/src/app/server .  
  
# Build the server for alpine, executable name: alphabets  
RUN go get  
RUN GOOS=linux GOARCH=amd64 CGO_ENABLED=0 go build -o alphabets  
  
### Small container to execute the server  
# Small container to run the app  
FROM alpine  
  
COPY \--from=server /go/src/github.com/tsauvajon/ws-blockchain/server /root/  
  
# Run the "./server" command when the container starts  
WORKDIR /root/  
ENTRYPOINT ./alphabets  
  
# Listen to 3333  
EXPOSE 3333

