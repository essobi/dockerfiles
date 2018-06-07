FROM ubuntu:14.04  
RUN apt-get update  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install php5-cli php5-curl
php5-memcached curl nmap  
  
# copy php scripts  
RUN mkdir -p /var/www/php  
ADD php/* /var/www/php/  
ADD php/dashboards/* /var/www/php/dashboards/  
  
# extract etcdctl  
ADD etcd-v3.0.6-linux-amd64.tar.gz /  
RUN mv etcd-v3.0.6-linux-amd64/etcdctl /usr/local/bin  
RUN rm -r etcd-v3.0.6-linux-amd64  
  
# provide a generic command since the container has several entry points  
CMD ['/bin/bash']  

