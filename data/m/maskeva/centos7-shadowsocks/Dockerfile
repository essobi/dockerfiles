FROM centos  
  
MAINTAINER Maskeva <zhongguoyinhang_17@qq.com>  
  
RUN yum -y update; yum clean all  
RUN yum install -y m2crypto openssl-devel && yum clean all  
RUN yum -y install python-setuptools && easy_install pip  
RUN pip install shadowsocks  
  
#ENV SS_ADDR 0.0.0.0  
ENV SS_PORT 9528  
ENV SS_PASSWORD 123456  
ENV SS_METHOD aes-256-cfb  
#ENV SS_TIMEOUT 300  
ADD shadowsocks.json /root/  
ADD start.sh /usr/bin/start.sh  
RUN chmod 755 /usr/bin/start.sh  
  
EXPOSE $SS_PORT  
  
CMD ["sh", "-c", "start.sh"]  

