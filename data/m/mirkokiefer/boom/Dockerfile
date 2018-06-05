  
FROM mirkokiefer/ubuntu-base  
  
RUN echo deb http://archive.ubuntu.com/ubuntu precise main universe >
/etc/apt/sources.list  
RUN echo deb http://archive.ubuntu.com/ubuntu precise-updates main universe >>
/etc/apt/sources.list  
RUN apt-get update  
  
RUN apt-get install -y golang  
  
RUN go get github.com/rakyll/boom  
  
ENTRYPOINT ["/usr/lib/go/bin/boom"]  

