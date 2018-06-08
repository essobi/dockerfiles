FROM golang:1.8  
MAINTAINER tinyproxy <tinyproxy@gmail.com>  
  
# shadowsocks settings  
ENV SHADOWSOCKS_SERVER=""  
ENV SHADOWSOCKS_PORT=""  
ENV SHADOWSOCKS_CIPHER="aes-256-cfb"  
ENV SHADOWSOCKS_PASSWORD=""  
ENV SHADOWSOCKS_TIMEOUT="300"  
# shadowsocks settings end  
RUN go get github.com/shadowsocks/shadowsocks-go/cmd/shadowsocks-local  
RUN apt-get update  
RUN apt-get install -y polipo supervisor  
EXPOSE 8123  
EXPOSE 1080  
COPY ./conf.d /etc/supervisor/conf.d  
COPY ./start.sh /start.sh  
CMD supervisord -n -c /etc/supervisor/supervisord.conf  

