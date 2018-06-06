FROM alpine:latest  
MAINTAINER Rowan Carr (https://github.com/rowancarr)  
  
ADD https://github.com/coreos/etcd/releases/download/v2.2.1/etcd-v2.2.1-linux-
amd64.tar.gz /tmp/etcd-v2.2.1-linux-amd64.tar.gz  
RUN tar -zxvf /tmp/etcd-v2.2.1-linux-amd64.tar.gz \  
&& mv etcd-v2.2.1-linux-amd64/etcd* /usr/local/bin/  
  
EXPOSE 2379 4001  
ENTRYPOINT ["/usr/local/bin/etcd"]  
CMD [ "-advertise-client-urls", "http://0.0.0.0:2379","-listen-client-urls",
"http://0.0.0.0:2379,http://0.0.0.0:4001", "-listen-peer-urls",
"http://0.0.0.0:2380" ]  

