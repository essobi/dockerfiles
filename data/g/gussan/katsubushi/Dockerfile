FROM golang:alpine  
MAINTAINER gussan <egussan@gmail.com>  
RUN apk \--update add git curl make  
RUN go get github.com/kayac/go-katsubushi && \  
cd ${GOPATH}/src/github.com/kayac/go-katsubushi && \  
make get-dep-on-ci && make get-deps && make && \  
cp cmd/katsubushi/katsubushi ${GOPATH}/bin  
  
ENV worker_id 1  
EXPOSE 11212  
CMD ["sh", "-c", "exec ${GOPATH}/bin/katsubushi -worker-id $worker_id"]  

