FROM centos:7  
# nprobe  
MAINTAINER Matthew McKenzie <matthew.mckenzie@rungeict.com>  
  
COPY resources/ /  
  
RUN yum -y install epel-release && \  
yum -y install libdnet pfring nprobe libnetfilter_queue && \  
yum -y clean all && \  
chmod +x /docker-entrypoint.sh  
  
EXPOSE 2055  
ENTRYPOINT /docker-entrypoint.sh  

