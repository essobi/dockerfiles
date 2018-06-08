FROM mastodonc/basejava  
  
RUN curl -s
http://apache.mirrors.pair.com/zookeeper/zookeeper-3.4.6/zookeeper-3.4.6.tar.gz
|\  
tar -xzf - -C / --transform 's@\\([a-z-]*\\)-[0-9\\.]*@\1@'  
  
EXPOSE 2181 2888 3888  
ADD start-zookeeper.sh /start-zookeeper  
  
CMD ["/bin/bash","/start-zookeeper"]  

