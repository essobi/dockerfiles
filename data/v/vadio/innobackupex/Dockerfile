FROM ubuntu:14.04  
RUN apt-key adv --keyserver ha.pool.sks-keyservers.net --recv-keys
430BDF5C56E7C94E848EE60C1C4CBDCDCD2EFD2A  
  
RUN echo 'deb http://repo.percona.com/apt trusty main' >
/etc/apt/sources.list.d/percona.list  
  
RUN apt-get update \  
&& apt-get install -y percona-xtrabackup  
  
ENTRYPOINT ["innobackupex"]  
  

