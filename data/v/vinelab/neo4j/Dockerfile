FROM vinelab/base  
MAINTAINER Abed Halawi <abed.halawi@vinelab.com>  
  
ENV NEO4J_VERSION 2.2.1  
# Install openjdk 1.7.0  
RUN yum install -y java-1.7.0-openjdk  
RUN yum install -y tar  
  
# Install Neo4j $NEO4J_VERSION in /var/lib/neo4j  
RUN mkdir /var/lib/neo4j  
RUN wget http://dist.neo4j.org/neo4j-community-$NEO4J_VERSION-unix.tar.gz  
RUN tar zxf neo4j-community-$NEO4J_VERSION-unix.tar.gz  
RUN cp -r neo4j-community-$NEO4J_VERSION/* /var/lib/neo4j  
RUN export NEO4J_HOME=/var/lib/neo4j  
  
## turn on indexing: http://chrislarson.me/blog/install-neo4j-graph-database-
ubuntu  
## enable neo4j indexing, and set indexable keys to name,age  
RUN sed -i "s|#node_auto_indexing|node_auto_indexing|g"
/var/lib/neo4j/conf/neo4j.properties  
RUN sed -i "s|#node_keys_indexable|node_keys_indexable|g"
/var/lib/neo4j/conf/neo4j.properties  
  
# Configure supervisord to manage the Neo4j process  
ADD neo4j.ini /etc/supervisord.d/  
RUN sed -i
's|;environment=KEY="value"|environment=JAVA_HOME="/usr/lib/jvm/jre-
openjdk/"|g' /etc/supervisord.conf  
  
ADD launch.sh /  
RUN chmod +x /launch.sh  
  
# clean sources  
RUN yum clean all  
RUN rm neo4j-community-$NEO4J_VERSION-unix.tar.gz  
RUN rm -rf neo4j-community-$NEO4J_VERSION  
  
# Entrypoint  
CMD ["/bin/bash", "-c", "/launch.sh"]  

