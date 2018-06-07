FROM golang:1.4  
RUN mkdir -p /tmp/build  
ADD hello-world.go /tmp/build/  
WORKDIR /tmp/build  
RUN go build hello-world.go  
RUN echo whoami  
RUN echo whoami  
CMD tar -czf - hello-world  

