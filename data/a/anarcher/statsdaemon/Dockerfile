FROM busybox:ubuntu-14.04  
EXPOSE 8125/udp  
  
ENV ADDRESS 127.0.0.1:8125  
ENV GRAPHITE 127.0.0.1:2003  
ENV FLUSH_INTERVAL 60  
ENV PERCENTILES 90,99  
#ENV PREFIX (blank)  
ADD
https://github.com/bitly/statsdaemon/releases/download/v0.7.1/statsdaemon-0.7.1.linux-
amd64.go1.4.2.tar.gz .  
RUN tar xzvf statsdaemon-0.7.1.linux-amd64.go1.4.2.tar.gz -C /tmp/  
RUN cp /tmp/statsdaemon-0.7.1.linux-amd64.go1.4.2/statsdaemon /bin/  
  
CMD exec /bin/statsdaemon --address=$ADDRESS \  
\--graphite=$GRAPHITE \  
\--prefix=$PREFIX \  
\--flush-interval=$FLUSH_INTERVAL \  
$(echo $PERCENTILES | tr , '\n' | xargs printf \-- '--percent-threshold=%s ')  

