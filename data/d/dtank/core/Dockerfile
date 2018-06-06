FROM ubuntu:latest  
  
MAINTAINER benharker@mac.com  
  
#install the basics  
RUN apt-get update && apt-get install -y curl wget nano jq facter etcd ;  
#&& rm -rf /var/lib/apt/lists/*  
#let's grab etcd  
#RUN curl -L
https://github.com/coreos/etcd/releases/download/v2.2.4/etcd-v2.2.4-linux-
amd64.tar.gz -o etcd-v2.2.4-linux-amd64.tar.gz && tar xzvf etcd-v2.2.4-linux-
amd64.tar.gz && mv etcd-v2.2.4-linux-amd64/./etcd* /usr/local/bin/ ;  
#make etcd data-dir  
RUN mkdir -p /var/dtank/etcd ;  
  
#RUN echo "/usr/local/bin/etcd >>/var/log/etcd.log 2>&1" >>
/usr/local/bin/run-etcd ;  
COPY ./run-etcd /usr/local/bin/run-etcd  
RUN chmod -Rv 777 /usr/local/bin/* ;  
  
EXPOSE 4001  
EXPOSE 2380  
EXPOSE 2379  
EXPOSE 7001  
CMD ["/bin/bash"]  

