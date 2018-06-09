FROM jxtadoop/edge  
  
MAINTAINER Franck Besnard <franck@besnard.mobi>  
  
RUN cd /opt/jxtadoop-1.0.0/etc; sed -i
's/<name>hadoop.p2p.datanode.relay<\/name><value>false<\/value>/<name>hadoop.p2p.datanode.relay<\/name><value>true<\/value>/g'
hdfs-p2p.xml  

