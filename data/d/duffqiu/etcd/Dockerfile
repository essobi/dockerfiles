FROM centos:latest  
MAINTAINER duffqiu@gmail.com  
  
RUN yum -y update  
RUN yum install -y wget tar gawk  
  
RUN wget --no-cookies --no-check-certificate
https://github.com/coreos/etcd/releases/download/v2.0.9/etcd-v2.0.9-linux-
amd64.tar.gz  
  
RUN tar zxf etcd-v2.0.9-linux-amd64.tar.gz  
  
RUN mv etcd-v2.0.9-linux-amd64 etcd  
  
RUN rm -rf etcd-v2.0.9-linux-amd64.tar.gz  
  
COPY start-standalone /etcd/  
RUN chmod +x /etcd/start-standalone  
  
COPY start-local-cluster /etcd/  
RUN chmod +x /etcd/start-local-cluster  
  
WORKDIR etcd  
  
#for standalone  
EXPOSE 4001  
#for local cluster  
EXPOSE 4002 4003  
#node proxy  
EXPOSE 9001  
#must set this entrypoint to use bash, otherwise it can't run the bash script
command  
ENTRYPOINT ["/bin/bash", "-c"]  
  
CMD ["/etcd/start-standalone"]  

