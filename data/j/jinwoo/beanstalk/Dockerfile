FROM ubuntu:14.04  
#ARG BT_VERSION  
ENV BT_VERSION 1.10  
RUN echo "BeanstalkD version = ${BT_VERSION}"  
  
RUN apt-get update && apt-get install -y build-essential wget zip  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
WORKDIR /usr/src  
RUN wget https://github.com/kr/beanstalkd/archive/v${BT_VERSION}.zip && unzip
v${BT_VERSION}.zip \  
&& cd beanstalkd-${BT_VERSION} && make -j"$(nproc)" && make install \  
&& mkdir /data && cd /usr/src && rm -rf /usr/src/beanstalkd-${BT_VERSION}  
  
VOLUME ["/data"]  
EXPOSE 11300  
CMD ["/usr/local/bin/beanstalkd", "-f", "60000", "-b", "/data"]  
  

