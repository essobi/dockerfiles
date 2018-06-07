FROM alpine:3.4  
MAINTAINER szuta@illinois.edu  
RUN apk --update --no-cache add \  
g++ \  
git \  
mariadb-dev \  
bash \  
automake \  
libtool \  
autoconf \  
make \  
&& git clone https://github.com/akopytov/sysbench.git \  
&& cd /sysbench && ./autogen.sh && ./configure && make && make install  
ENTRYPOINT ["/usr/local/bin/sysbench"]  

