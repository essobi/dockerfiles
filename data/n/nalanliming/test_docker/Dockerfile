FROM golang:1.8.3  
USER root  
RUN go get github.com/astaxie/beego \  
&& go get github.com/beego/bee \  
&& go get github.com/shirou/gopsutil \  
&& go get golang.org/x/sys/unix \  
&& go version \  
&& go env  
WORKDIR /go/src/huantian.com/ww/test_docker/  
COPY . .  
EXPOSE 28080  
CMD ["bee", "run"]  

