FROM mastodonc/basejava  
  
RUN curl -sL
https://download.elastic.co/kibana/kibana/kibana-4.3.0-linux-x64.tar.gz | \  
tar -xzf - -C / --transform 's@\\([a-z-]*\\)-[0-9\\.]*@\1@'  
  
ADD start-kibana.sh /start-kibana  
  
EXPOSE 5601  
CMD ["/bin/bash","/start-kibana"]  

