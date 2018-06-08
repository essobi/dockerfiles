FROM nsqio/nsq:latest  
  
  
RUN cd /gopath/src/github.com/bitly/nsq/apps/nsqlookupd && go build .  
RUN cd /gopath/src/github.com/bitly/nsq/apps/nsqd && go build .  
RUN mkdir /data  
EXPOSE 4160  
EXPOSE 4161  
EXPOSE 4150  
EXPOSE 4151  
ADD run.sh /usr/local/bin/  
  
ENTRYPOINT ["/usr/local/bin/run.sh"]  

