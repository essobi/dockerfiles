# Dockerfile to run KairosDB on Cassandra. Configuration is done through
environment variables.  
#  
# The following environment variables can be set  
#  
# $CASS_HOSTS [kairosdb.datastore.cassandra.host_list] (default:
localhost:9160)  
# Cassandra seed nodes (host:port,host:port)  
#  
# $REPFACTOR [kairosdb.datastore.cassandra.replication_factor] (default: 1)  
# Desired replication factor in Cassandra  
#  
# $PORT_TELNET [kairosdb.telnetserver.port] (default: 4242)  
# Port to bind for telnet server  
#  
# $PORT_HTTP [kairosdb.jetty.port] (default: 8080)  
# Port to bind for http server  
#  
# $PORT_CARBON_TEXT [kairosdb.carbon.text.port] (default: 2003)  
# Port to bind for carbon text server  
#  
# $PORT_CARBON_PICKLE [kairosdb.carbon.pickle.port] (default: 2004)  
# Port to bind for carbon pickle server  
#  
# Sample Usage:  
# docker run -P -e "CASS_HOSTS=192.168.1.63:9160" -e "REPFACTOR=1"
enachb/archlinux-kairosdb  
  
FROM ngty/archlinux-jdk7  
MAINTAINER Mesosphere support@mesosphere.io  
  
EXPOSE 8080  
EXPOSE 4242  
EXPOSE 2003  
EXPOSE 2004  
  
# Install KAIROSDB  
RUN cd /opt; \  
curl -L
https://github.com/kairosdb/kairosdb/releases/download/v1.1.0/kairosdb-1.1.0-1.tar.gz
| \  
tar zxfp - && \  
curl -L https://github.com/kairosdb/kairos-
carbon/releases/download/v1.0-1/kairos-carbon-1.0.tar.gz | \  
tar zxfp -  
  
ADD kairosdb.properties /tmp/kairosdb.properties  
ADD runKairos.sh /usr/bin/runKairos.sh  
  
# Run kairosdb in foreground on boot  
ENTRYPOINT [ "/usr/bin/runKairos.sh" ]  

