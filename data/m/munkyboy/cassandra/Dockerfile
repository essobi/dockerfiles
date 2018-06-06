FROM munkyboy/java:quantal_7  
  
# add source for cassandra  
RUN echo "deb http://debian.datastax.com/community stable main" | tee -a
/etc/apt/sources.list.d/cassandra.sources.list  
RUN apt-key adv --keyserver pgp.mit.edu --recv-keys 350200F2B999A372  
RUN apt-get update -o
Dir::Etc::sourcelist="sources.list.d/cassandra.sources.list" -o
Dir::Etc::sourceparts="-" -o APT::Get::List-Cleanup="0"  
  
# install cassandra  
RUN apt-get install -yq dsc12=1.2.15-1 cassandra=1.2.15  
RUN sed -i -e "s/^rpc_address.*/rpc_address: 0.0.0.0/"
/etc/cassandra/cassandra.yaml  
  
RUN apt-get install -yq net-tools  
  
VOLUME ["/var/lib/cassandra", "/var/log/cassandra"]  
EXPOSE 9160  
ADD start.sh /usr/local/bin/start.sh  
CMD /usr/local/bin/start.sh  

