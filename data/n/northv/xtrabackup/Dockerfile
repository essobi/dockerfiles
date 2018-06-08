FROM debian:wheezy  
  
ENV XTRABACKUP_VERSION 2.2.11-1.wheezy  
  
# Install percona xtrabackup  
RUN \  
echo "deb http://repo.percona.com/apt wheezy main" >
/etc/apt/sources.list.d/percona.list \  
&& echo "deb-src http://repo.percona.com/apt wheezy main" >>
/etc/apt/sources.list.d/percona.list \  
&& apt-key adv --keyserver keys.gnupg.net --recv-keys 1C4CBDCDCD2EFD2A \  
&& apt-get update && apt-get install -y --no-install-recommends \  
percona-xtrabackup=$XTRABACKUP_VERSION \  
qpress \  
&& rm -rf /var/lib/apt/lists/* \  
  
CMD ["bash"]  

