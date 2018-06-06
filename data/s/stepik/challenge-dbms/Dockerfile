FROM stepic/challenge-base  
MAINTAINER Mark Zaslavskiy <mark.zaslavskiy@gmail.com>  
  
COPY mongodb_key.asc neo4j_key.asc /root/  
  
RUN apt-key add /root/mongodb_key.asc \  
&& apt-key add /root/neo4j_key.asc  
  
# Add and configure APT repositories  
RUN echo "deb [ arch=amd64 ] http://repo.mongodb.org/apt/ubuntu
trusty/mongodb-org/3.4 multiverse" | tee /etc/apt/sources.list.d/mongodb-
org-3.4.list \  
# Neo4j  
&& echo "deb https://debian.neo4j.org/repo stable/" | tee
/etc/apt/sources.list.d/neo4j.list \  
# Oracle JDK 1.8  
&& add-apt-repository -y ppa:webupd8team/java \  
&& echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-
selections \  
&& echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-
selections  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
mongodb-org \  
oracle-java8-installer cypher-shell neo4j=3.2.3 \  
python3-numpy \  
&& pip3 install pymongo py2neo \  
&& rm -rf /var/lib/apt/lists/*  
  
# Create the data directory for MongoDB  
RUN mkdir -p /data/db  
  
# Configure Neo4j  
RUN echo "dbms.security.auth_enabled=false" | tee -a /etc/neo4j/neo4j.conf  

