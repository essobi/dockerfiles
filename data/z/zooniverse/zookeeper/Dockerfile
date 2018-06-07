FROM zooniverse/java  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get -y upgrade && \  
apt-get install -y zookeeper supervisor && \  
apt-get clean  
  
ADD start.sh /  
ADD supervisor.conf /etc/supervisor/conf.d/zookeeper.conf  
  
RUN mkdir -p /config && mv /etc/zookeeper/conf/zoo.cfg /config/zoo.cfg && ln
-s /config/zoo.cfg /etc/zookeeper/conf/zoo.cfg  
  
EXPOSE 2888 3888 2181  
  
ENTRYPOINT [ "/start.sh" ]  

