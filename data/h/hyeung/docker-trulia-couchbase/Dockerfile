From ubuntu:12.04  
### this Dockerfile is heavily borrowed from jamesdbloom / couchbase, the only
change is the version of couchbase  
MAINTAINER Hinling Yeung "hyeung@trulia.com"  
ADD http://cbfs-ext.hq.couchbase.com/couchbase-dist/couchbase-server-
enterprise_2.2.0_x86_64.deb /tmp/couchbase-server-enterprise_2.2.0_x86_64.deb  
  
RUN export DEBIAN_FRONTEND=noninteractive  
RUN apt-get update  
RUN apt-get -y install vim curl libssl0.9.8 librtmp0 python  
RUN dpkg -i /tmp/couchbase-server-enterprise_2.2.0_x86_64.deb  
  
# remove couchbase install file  
RUN rm /tmp/couchbase-server-enterprise_2.2.0_x86_64.deb  
  
# add start scripts  
ADD start_couchbase.sh /start_couchbase.sh  
  
# Expose Web Administration Port, Couchbase API Port & Internal/External
Bucket Port  
EXPOSE 8091 8092 11210  

