FROM centos:7 as buildimg  
  
RUN mkdir -p /app/data  
WORKDIR /app  
  
ENV GOPATH /app/data  
ENV GOROOT /app/go  
  
RUN yum install git -y  
RUN curl https://dl.google.com/go/go1.10.1.linux-amd64.tar.gz > go.tar.gz  
RUN tar zxf go.tar.gz  
RUN PATH=$GOROOT/bin:$PATH go get github.com/RedisLabs/sentinel_tunnel  
  
FROM scratch  
COPY \--from=buildimg /app/data/bin/sentinel_tunnel /sentinel_tunnel  

