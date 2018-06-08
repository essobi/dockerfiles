FROM nyasara/docker-managementbase  
  
# Get etcdctl  
RUN curl -L
https://github.com/coreos/etcd/releases/download/v0.5.0-alpha.2/etcd-v0.5.0-alpha.2-linux-
amd64.tar.gz -o etcd-v0.5.0-alpha.2-linux-amd64.tar.gz \  
&& tar xzvf etcd-v0.5.0-alpha.2-linux-amd64.tar.gz \  
&& cd etcd-v0.5.0-alpha.2-linux-amd64 \  
&& mkdir /working \  
&& cp etcdctl /working  
  
# Declare the volume for where the config will be  
VOLUME /etc/etcdwatcher  
WORKDIR /working  
  
# Copy the worker script in and make it executable  
COPY etcd-watch.sh /working/  
RUN chmod 550 /working/etcd-watch.sh  
  
# Run the watch script forever  
CMD ["/bin/bash", "/working/etcd-watch.sh"]  

