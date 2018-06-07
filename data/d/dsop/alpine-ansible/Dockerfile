FROM dsop/alpine-base  
  
RUN apk --update add ansible wget ca-certificates  
  
RUN mkdir /opt/ && \  
cd /opt && \  
wget https://github.com/couchbase/couchbase-cli/archive/4.1.2.tar.gz && \  
tar xzf 4.1.2.tar.gz && \  
ln -s /opt/couchbase-cli-4.1.2/couchbase-cli /usr/local/bin/couchbase-cli  
  
RUN mkdir /etc/ansible && echo "localhost ansible_connection=local" >
/etc/ansible/hosts  
  
CMD ["/bin/bash"]  

