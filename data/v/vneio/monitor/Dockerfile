FROM clojure  
MAINTAINER Ivan Yaroslavov Stefanov <ivan.yaroslavov@vne.io>  
  
COPY . /opt/vne-monitor-src  
  
RUN cd /opt/vne-monitor-src \  
&& lein clean \  
&& lein uberjar \  
&& cd / \  
&& mkdir -p /opt/vne-monitor \  
&& mkdir -p /opt/vne-monitor/logs \  
&& cp /opt/vne-monitor-src/target/vne-monitor.jar /opt/vne-monitor \  
&& cp /opt/vne-monitor-src/.lein-env /opt/vne-monitor \  
&& rm -rf /opt/vne-monitor-src  
  
WORKDIR /opt/vne-monitor  
CMD java -jar vne-monitor.jar  

