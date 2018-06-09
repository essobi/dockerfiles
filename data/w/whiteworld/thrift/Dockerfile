FROM ubuntu:14.04.2  
MAINTAINER White World "ljq258@gmail.com"  
ENV THRIFT_VERSION 0.5.0  
RUN echo "deb http://mirrors.aliyun.com/ubuntu/ trusty main restricted
universe multiverse \ndeb http://mirrors.aliyun.com/ubuntu/ trusty-security
main restricted universe multiverse \ndeb http://mirrors.aliyun.com/ubuntu/
trusty-updates main restricted universe multiverse \ndeb
http://mirrors.aliyun.com/ubuntu/ trusty-proposed main restricted universe
multiverse \ndeb http://mirrors.aliyun.com/ubuntu/ trusty-backports main
restricted universe multiverse \ndeb-src http://mirrors.aliyun.com/ubuntu/
trusty main restricted universe multiverse \n deb-src
http://mirrors.aliyun.com/ubuntu/ trusty-security main restricted universe
multiverse \ndeb-src http://mirrors.aliyun.com/ubuntu/ trusty-updates main
restricted universe multiverse \ndeb-src http://mirrors.aliyun.com/ubuntu/
trusty-proposed main restricted universe multiverse \ndeb-src
http://mirrors.aliyun.com/ubuntu/ trusty-backports main restricted universe
multiverse" > /etc/apt/sources.list \  
&& apt-get update  
RUN echo "y"| apt-get install build-essential  
RUN echo "y"| apt-get install wget  
RUN wget http://archive.apache.org/dist/incubator/thrift/$THRIFT_VERSION-
incubating/thrift-$THRIFT_VERSION.tar.gz -O thrift.tar.gz  
RUN tar zxf thrift.tar.gz \  
&& cd thrift-$THRIFT_VERSION \  
&& ./configure --with-php=no --with-php_extension=no --with-python=no \  
&& make \  
&& make install  
  
ENTRYPOINT ["thrift"]  

