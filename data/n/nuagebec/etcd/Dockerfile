FROM mikefaille/go-base:latest  
MAINTAINER Michaël Faille <michael@faille.pw>  
# Let's install etcd and etcdctl (from source).  
ADD supervisor-etcd.conf /etc/supervisor/conf.d/etcd.conf  
ADD start-etcd.sh /data/start-etcd.sh  
RUN chmod +x /data/start-etcd.sh  
  
RUN cd /opt && git clone \--depth=1 https://github.com/coreos/etcd.git && cd
/opt/etcd && \  
./build && mv bin/* /usr/local/bin && \  
GOPATH=/opt/etcd/gopath:$GOPATH go build etcdctl/main.go && mv main
/usr/local/bin/etcdctl && \  
rm -R /opt/etcd  
  
# as seen on https://github.com/coreos/etcd/blob/master/Dockerfile  
EXPOSE 4001 7001 2379 2380  
#ADD docker_env_file /data/docker_env_file  
CMD ["/data/run.sh"]  

