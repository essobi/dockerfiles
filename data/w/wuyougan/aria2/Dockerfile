FROM alpine:3.4  
MAINTAINER yewenju <wuyougan@163.com>  
  
# 安装所需的包  
RUN apk add --no-cache aria2 bash curl tzdata && \  
rm -f /etc/localtime && \  
ln -s /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \  
echo "Asia/Shanghai" > /etc/timezone && \  
adduser -D -g '' aria2  
  
EXPOSE 6800  
USER aria2  
  
CMD ["aria2c", "--conf-path=/etc/aria2/aria2.conf"]  
  

