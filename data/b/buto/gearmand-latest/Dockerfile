#Build gearman on ubuntu 14.04 which has gearman 1.11 as oppssed to RPM
distros which have 1.08  
#you can use sqllite for persistance backend, which means queues can be
resumed even if gearman dies  
FROM ubuntu:14.04  
MAINTAINER Jujhar Singh <jujhar@jujhar.com>  
  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive \  
&& apt-get install -y \  
build-essential \  
binutils-doc \  
software-properties-common \  
libboost-all-dev \  
gperf \  
libevent-dev \  
uuid-dev \  
wget \  
libmysqlclient-dev \  
libmemcached-dev \  
libsqlite3-dev \  
libpq-dev \  
libdrizzle-dev \  
sqlite \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
#can be overridden  
VOLUME ["/gearman"]  
  
# Install Gearman Job Server  
#RUN wget
https://launchpad.net/gearmand/1.2/1.1.12/+download/gearmand-1.1.12.tar.gz  
#grab the build locally in case launchpad.net is inaccessable  
COPY gearmand-1.1.15.tar.gz /gearman/gearmand-1.1.15.tar.gz  
RUN tar xzf /gearman/gearmand-1.1.15.tar.gz -C /tmp  
RUN cd /tmp/gearmand-1.1.15 && ./configure && make && make install  
  
#have a log/db that could be potentially mounted locally by --volume  
RUN ["/bin/touch", "/gearman/gearmand.log", "/gearman/gearmand.sqlite"]  
  
#init sqlite db with a gearman schema  
#RUN /usr/bin/sqlite /gearman/gearmand.sqlite "CREATE TABLE
gearman_queue(unique_key TEXT PRIMARY KEY,function_name TEXT,when_to_run
INTEGER,priority INTEGER,data BLOB);"  
EXPOSE 4730  
#ENTRYPOINT [ "/usr/local/sbin/gearmand","--verbose=NOTICE", "--job-
retries=4", "--log-file=/gearman/gearmand.log", "--threads=8", "--
libsqlite3-db=/gearman/gearmand.sqlite" ]  
ENTRYPOINT [ "/usr/local/sbin/gearmand","--verbose=NOTICE", "--job-retries=4",
"--log-file=/gearman/gearmand.log", "--threads=8" ]  
#ENTRYPOINT ["/bin/bash"]  

