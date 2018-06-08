FROM urelx/centos6-epel  
MAINTAINER Yuu Yamanaka <yuu@relx.jp>  
  
RUN yum update -y && yum install -y pdns-recursor  
  
EXPOSE 53 53/udp  
VOLUME ["/conf.d"]  
  
ENTRYPOINT ["/usr/sbin/pdns_recursor", "--daemon=no", "--config-dir=/conf.d",
"--allow-from=0.0.0.0/0", "--local-address=0.0.0.0"]  

