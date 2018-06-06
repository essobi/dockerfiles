FROM ontouchstart/docker-golang-base  
MAINTAINER ontouchstart <ontouchstart@gmail.com>  
  
RUN go get github.com/ontouchstart/cayley  
RUN echo "graph.Vertex().All()" | cayley repl
--dbpath=/src/github.com/google/cayley/testdata.nt  

