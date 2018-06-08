FROM frodenas/java7  
MAINTAINER sayjava <duketek.developer@gmail.com>  
  
# Install and configure Neo4j 2.1.2  
RUN cd /tmp && \  
wget http://dist.neo4j.org/neo4j-community-2.1.2-unix.tar.gz && \  
tar xzvf neo4j-community-2.1.2-unix.tar.gz && \  
mv /tmp/neo4j-community-2.1.2/ /neo4j && \  
sed -e
's/^org.neo4j.server.database.location=.*$/org.neo4j.server.database.location=\/opt\/dbdata/'
-i /neo4j/conf/neo4j-server.properties && \  
sed -e
's/^#org.neo4j.server.webserver.address=.*$/org.neo4j.server.webserver.address=0.0.0.0/'
-i /neo4j/conf/neo4j-server.properties && \  
echo "remote_shell_host=0.0.0.0" >> /neo4j/conf/neo4j.properties && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Add scripts  
ADD scripts /scripts  
ADD scripts /cmds  
RUN chmod +x /scripts/*.sh  
RUN chmod +x /cmds/*.sh  
  
ENTRYPOINT ["/cmds/bootstrap.sh"]  
CMD [""]  
  
# Expose listen port  
EXPOSE 7474  
EXPOSE 1337

