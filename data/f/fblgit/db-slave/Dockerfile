# docker percona cluster-slave  
FROM ubuntu:trusty  
# Upgrade  
ENV HEARTBEAT /mnt/cluster_hb  
ENV HB_PERIOD 10  
ENV CLUSTER_NAME FBL  
VOLUME /data  
  
RUN apt-get update && apt-get upgrade -y && apt-get dist-upgrade -y  
ENV DEBIAN_FRONTEND noninteractive  
RUN echo "deb http://repo.percona.com/apt trusty main" >>
/etc/apt/sources.list.d/percona.list  
RUN echo "deb-src http://repo.percona.com/apt trusty main" >>
/etc/apt/sources.list.d/percona.list  
RUN apt-key adv --keyserver keys.gnupg.net --recv-keys 1C4CBDCDCD2EFD2A  
RUN apt-get update  
RUN apt-get install -y percona-xtradb-cluster-56 qpress xtrabackup  
RUN apt-get install -y python-software-properties vim wget curl netcat
supervisor  
ADD /scripts/ /data/  
RUN chmod 755 /data/*.sh  
  
RUN /data/install.sh  
  
CMD ["/data/start.sh"]  

