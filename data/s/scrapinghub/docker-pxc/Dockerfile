FROM ubuntu:precise  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-key adv --keyserver keys.gnupg.net --recv-keys 1C4CBDCDCD2EFD2A  
RUN echo "deb http://repo.percona.com/apt squeeze main" >>
/etc/apt/sources.list  
# RUN apt-get update && apt-get install -yq lsof libaio1 libreadline5 socat
xtrabackup rsync libssl0.9.8 pv qpress gzip procps gdb  
RUN apt-get update && apt-get install -yq percona-xtradb-cluster-server-5.6
xtrabackup rsync  
  
EXPOSE 3306 4567 4568  
ADD entrypoint.sh /  
RUN chmod 755 /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["start"]  

