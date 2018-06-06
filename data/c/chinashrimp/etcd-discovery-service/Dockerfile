FROM microbox/scratch  
  
ADD etcd-v2.1.1-linux-amd64/etcd /bin/etcd  
  
# exclude the cli tool to reduce the size of the image  
ADD etcd-v2.1.1-linux-amd64/etcdctl /bin/etcdctl  
  
RUN set -x \  
&& chmod +x /bin/etcd*  
  
VOLUME ["/data"]  
  
EXPOSE 2379  
ENTRYPOINT ["/bin/etcd"]  
  
CMD ["-data-dir=/data", "-name=register", "-listen-client-
urls=http://0.0.0.0:2379", "-advertise-client-urls=http://0.0.0.0:2379"]  

