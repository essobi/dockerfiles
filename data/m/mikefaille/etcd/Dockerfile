FROM mikefaille/go-base:latest  
MAINTAINER Michaël Faille <michael@faille.pw>  
# Let's install etcd and etcdctl (from source).  
ADD supervisor-etcd.conf /etc/supervisor/conf.d/etcd.conf  
  
RUN cd /opt && git clone \--depth=1 https://github.com/coreos/etcd.git && cd
/opt/etcd && \  
PATH=/usr/local/go/bin:$PATH ./build && mv bin/* /usr/local/bin && \  
rm -R /opt/etcd && \  
cd /opt && git clone \--depth=1 https://github.com/coreos/etcdctl/ && cd
/opt/etcdctl && \  
PATH=/usr/local/go/bin:$PATH ./build && mv bin/* /usr/local/bin && \  
rm -R /opt/etcdctl  
  
EXPOSE 4001 7001  
CMD ["/data/run.sh"]  

