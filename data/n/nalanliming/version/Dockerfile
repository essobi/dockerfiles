FROM golang:1.8.3  
USER root  
ENV WWRUNMODE "prod"  
RUN go get github.com/astaxie/beego \  
&& go get github.com/beego/bee \  
&& go version \  
&& go env  
WORKDIR /go/src/huantian.com/ww/version/  
COPY . .  
EXPOSE 18000  
CMD ["bee", "run"]  

