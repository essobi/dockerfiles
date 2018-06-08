FROM antik486/jdk  
MAINTAINER antik486 <antik486@gmail.com>  
  
RUN curl https://packagecloud.io/install/repositories/basho/riak/script.rpm |
bash  
RUN yum -y install riak-2.0.2-1.el7.centos.x86_64  
  
RUN yum -y update  
RUN yum clean all  
  
RUN sed -i 's/127.0.0.1/0.0.0.0/' /etc/riak/riak.conf  
RUN sed -i 's/search = off/search = on/' /etc/riak/riak.conf  
  
EXPOSE 8098 8087 8985  
CMD /usr/sbin/riak start -l debug && tail -f /var/log/riak/*.log  

