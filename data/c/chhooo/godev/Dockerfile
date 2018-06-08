FROM golang:1.10.1  
MAINTAINER Chris <cenne1986@qq.com>  
  
RUN echo "created at 2017-07-01"  
RUN go get github.com/chrisho/mosquito  
RUN go get github.com/samuel/go-zookeeper/zk  
RUN go get github.com/sirupsen/logrus  
RUN go get github.com/go-redis/redis  
RUN go get github.com/jinzhu/gorm  
RUN go get golang.org/x/crypto/bcrypt  
RUN go get github.com/go-sql-driver/mysql  
RUN go get github.com/asaskevich/govalidator  
RUN go get github.com/garyburd/redigo/redis  
RUN go get github.com/gin-gonic/gin  
RUN go get github.com/rainbowism/osin  
RUN go get github.com/rainbowism/osin-redis  
RUN go get github.com/tommy351/gin-csrf  
RUN go get github.com/tommy351/gin-sessions  
RUN go get github.com/google/uuid  
RUN go get github.com/SebastiaanKlippert/go-wkhtmltopdf  
RUN go get github.com/robfig/cron  
RUN go get github.com/Shopify/sarama  
RUN go get github.com/bsm/sarama-cluster  
RUN go get golang.org/x/text  
  
  
#RUN cd ~ && git clone --recursive
https://github.com/wkhtmltopdf/wkhtmltopdf.git  
#RUN apt-get -y install qt5default qt5webkit  
#RUN apt-get update && apt-get install -y xfonts-75dpi libjpeg62-turbo
fontconfig libx11-6 libxext6 libxrender1 libxcb1 xfonts-base  
#RUN apt-get install -y xvfb  
#RUN cd ~ && wget
https://bitbucket.org/wkhtmltopdf/wkhtmltopdf/downloads/wkhtmltox-0.13.0-alpha-7b36694_linux-
jessie-amd64.deb \  
# && dpkg -i wkhtmltox-0.13.0-alpha-7b36694_linux-jessie-amd64.deb  
RUN cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime  

