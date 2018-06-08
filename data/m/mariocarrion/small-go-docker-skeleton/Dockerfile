# vim: set syntax=dockerfile:  
FROM golang:1.7.1  
COPY Makefile /  
WORKDIR /  
  
COPY ./ ./go/src/github.com/MarioCarrion/small-go-docker-skeleton  
RUN make gobuild  
  
CMD ["/bin/bash"]  

