FROM orctom/alpine:3.2  
MAINTAINER Hao Chen <orctom@gmail.com>  
  
RUN \  
mkdir /usr/local/consul \  
&& curl
https://releases.hashicorp.com/consul/0.8.3/consul_0.8.3_linux_amd64.zip -o
/tmp/consul.zip \  
&& unzip /tmp/consul.zip -d /usr/local/bin  
  
EXPOSE 8300 8301 8302 8400 8500 8600  
VOLUME /usr/local/consul  
  
ADD bootstrap.sh /bootstrap.sh  
  
ENTRYPOINT ["./bootstrap.sh"]  

