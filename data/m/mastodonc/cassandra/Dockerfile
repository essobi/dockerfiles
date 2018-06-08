FROM mastodonc/basejava  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update -qq && \  
DEBIAN_FRONTEND=noninteractive apt-get upgrade -qq -y && \  
DEBIAN_FRONTEND=noninteractive apt-get install -qq -y python2.7 && \  
DEBIAN_FRONTEND=noninteractive apt-get clean -qq && \  
DEBIAN_FRONTEND=noninteractive apt-get autoclean -qq  
  
RUN curl -sL
http://mirror.ox.ac.uk/sites/rsync.apache.org/cassandra/2.1.3/apache-
cassandra-2.1.3-bin.tar.gz | \  
tar -xzf - -C / --transform 's@\\([a-z-]*\\)-[0-9\\.]*@\1@'  
  
ADD start-cassandra.sh /start-cassandra  
  
############################################  
# Make Oracle JDK the default.  
  
CMD ["/bin/bash","/start-cassandra"]  
  
# 9042 is CQL, 9160 is thrift  
# TODO - remove thrift?  
EXPOSE 9042 9160  

