# Percona XtraDB Cluster  
FROM ubuntu:trusty  
MAINTAINER Peerasan Buranasanti (Patrickz) <peerasan@gmail.com>  
LABEL version="1.0"  
LABEL description="Percona XtraDB Cluster"  
  
CMD ["/bin/bash"]  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && apt-get upgrade -y && apt-get dist-upgrade -y  
RUN apt-get autoclean  
RUN apt-key adv --keyserver keys.gnupg.net --recv-keys 1C4CBDCDCD2EFD2A  
RUN echo "deb http://repo.percona.com/apt trusty main" >>
/etc/apt/sources.list.d/percona.list  
RUN echo "deb-src http://repo.percona.com/apt trusty main" >>
/etc/apt/sources.list.d/percona.list  
RUN apt-get update  
RUN apt-get install -y percona-xtradb-cluster-56 qpress xtrabackup  
RUN apt-get install -y python-software-properties vim wget curl netcat  
  
# listening  
EXPOSE 3306  
EXPOSE 4444  
EXPOSE 4567  
EXPOSE 4568  
ADD start.sh /start.sh  
RUN chmod 755 /start.sh  
CMD ["/start.sh"]  

