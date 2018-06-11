FROM centos  
MAINTAINER Yuu Yamanaka <yuu@relx.jp>  
  
RUN yum install -y unzip  
ADD https://dl.bintray.com/mitchellh/consul/0.3.0_linux_amd64.zip
/tmp/consul.zip  
RUN unzip /tmp/consul.zip -d /usr/local/bin/ && rm -f /tmp/consul.zip  
  
EXPOSE 8300 8301 8301/udp 8302 8302/udp 8400 8500 8600/udp  
VOLUME ["/data", "/conf.d"]  
  
ENTRYPOINT ["/usr/local/bin/consul", "agent", "-data-dir=/data", "-config-
dir=/conf.d", "-client=0.0.0.0"]  

