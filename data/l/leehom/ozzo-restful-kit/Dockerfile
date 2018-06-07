# Base image is in https://registry.hub.docker.com/_/golang/  
# Refer to https://blog.golang.org/docker for usage  
FROM golang:latest  
MAINTAINER leehom clh021@gmail.com  
  
# Install go-ozzo & All ozzo pkg  
RUN go get -u github.com/go-ozzo/ozzo-routing  
RUN go get -u github.com/go-ozzo/ozzo-config  
RUN go get -u github.com/go-ozzo/ozzo-dbx  
RUN go get -u github.com/go-ozzo/ozzo-validation  
RUN go get -u github.com/go-ozzo/ozzo-log  
RUN go get -u github.com/go-ozzo/ozzo-di  
RUN go get -u github.com/go-sql-driver/mysql  
  
# 尽可能包含所需的所有包到镜像中以节省境内用户的时间精力  
# install the starter kit  
RUN go get github.com/qiangxue/golang-restful-starter-kit  
RUN go get -u github.com/Masterminds/glide  
RUN cd $GOPATH/src/github.com/qiangxue/golang-restful-starter-kit && glide up
-u -s  
WORKDIR $GOPATH/src/github.com/qiangxue/golang-restful-starter-kit  
ADD start.sh /start.sh  
RUN chmod 755 /start.sh  
CMD ["/start.sh"]  
EXPOSE 8080  
#使用步骤  
#docker run --name postgres -d -p 5432:5432 -e POSTGRES_PASSWORD="postgres" -e
POSTGRES_DB="go_restful" postgres  
#docker run -d -p 8080:8080 --name restful --link postgres:postgres
leehom/ozzo-restful-kit #一般情况下的使用  
#docker run -it --rm -p 8080:8080 --name restful --link postgres:postgres
leehom/ozzo-restful-kit #短暂测试用  
#docker run -it -p 8080:8080 --name restful --link postgres:postgres
leehom/ozzo-restful-kit bash #调试使用  
#境内用户如需包含更多包，欢迎反馈，会酌情添加

