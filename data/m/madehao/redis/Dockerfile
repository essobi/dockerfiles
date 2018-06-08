FROM madehao/centos:6  
MAINTAINER madehao1983@sina.com  
  
# install nesessary software  
RUN yum -y install gcc  
  
# create user  
RUN groupadd redis -g 5000 \  
&& useradd -g redis -m redis -u 5000  
  
# get redis  
WORKDIR /tmp  
  
RUN curl http://download.redis.io/releases/redis-3.2.11.tar.gz -O  
  
# install redis  
RUN tar -zxvf redis-3.2.11.tar.gz  
  
WORKDIR /tmp/redis-3.2.11  
RUN make \  
&& make install  
  
# delete source file  
WORKDIR /  
RUN rm -fr /tmp/redis-3.2.11.tar.gz /tmp/redis-3.2.11  
  
USER redis  
CMD ["redis-server"]  
  

