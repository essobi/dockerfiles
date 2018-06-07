FROM extrasme/openjre  
MAINTAINER tech@extrasme.com  
  
RUN wget -q -O -
http://apache.mirrors.pair.com/zookeeper/zookeeper-3.4.6/zookeeper-3.4.6.tar.gz
| tar -xzf - -C / && mv /zookeeper-3.4.6 /zookeeper  
  
ADD zoo.cfg.template /zookeeper/conf/  
ADD *.sh /zookeeper/  
  
RUN chmod +x /zookeeper/*.sh  
  
EXPOSE 2181 2888 3888  
WORKDIR /zookeeper  
  
VOLUME ["/data"]  
CMD ["/zookeeper/start.sh"]  

