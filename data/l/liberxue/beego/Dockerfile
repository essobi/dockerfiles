  
FROM centos  
LABEL Name=beegodocker Version=0.0.1  
MAINTAINER liberxue liberxue@gmail.com  
RUN yum -y update  
RUN yum install -y golang  
RUN yum install -y git  
RUN mkdir /root/golang/  
ENV PATH $PATH:$GOPATH/bin  
ENV GOPATH=$HOME/root/golang/  
ENV GOBIN=$GOPATH/bin  
ENV PATH=$PATH:$GOBIN  
RUN source /etc/profile  
WORKDIR /root/golang/src/  
# Install beego & bee  
RUN go get -u github.com/astaxie/beego  
RUN go get -u github.com/beego/bee  
RUN go get github.com/BurntSushi/graphics-go/graphics  
RUN go get github.com/astaxie/beego/cache/memcache  
RUN go get github.com/astaxie/beego/cache/redis  
RUN go get github.com/astaxie/beego/context  
RUN go get github.com/astaxie/beego/orm  
RUN go get github.com/astaxie/beego/utils/pagination  
RUN go get github.com/go-sql-driver/mysql  
RUN go get github.com/gorilla/websocket  
RUN go get github.com/zheng-ji/goSnowFlake  
RUN go get github.com/oliamb/cutter  
ADD jfyk/ /root/golang/src/jfyk  
# EXPOSE 8080

