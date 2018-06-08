FROM pangpanglabs/golang  
MAINTAINER jang.jaehue@eland.co.kr  
  
ENV PKG_CONFIG_PATH /usr/lib/pkgconfig  
  
# install kafka client binary  
RUN git clone https://github.com/edenhill/librdkafka.git && \  
cd librdkafka && \  
./configure --prefix /usr && \  
make && \  
make install  
  
# install go packages  
RUN go get github.com/Shopify/sarama && \  
go get github.com/bsm/sarama-cluster && \  
go get github.com/jinzhu/configor && \  
go get github.com/go-sql-driver/mysql && \  
go get github.com/go-xorm/xorm && \  
go get github.com/confluentinc/confluent-kafka-go/kafka  

