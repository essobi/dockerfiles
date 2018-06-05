FROM ubuntu:14.04  
MAINTAINER hu zhengquan "zhengquan.hu@qq.com"  
RUN apt-get update && \  
apt-get install -y beanstalkd && \  
apt-get clean  
  
EXPOSE 11300  
ENTRYPOINT ["beanstalkd", "-p", "11300"]  
  
CMD ["-u", "nobody"]  

