FROM ubuntu:trusty  
  
MAINTAINER Joaquim Pedro Silveira <pedroxs@gmail.com>  
  
ENV LANG=C.UTF-8  
  
RUN apt-get update \  
&& apt-get install -y dnsutils wget curl git vim lynx ldap-utils mysql-client
\  
&& echo "deb http://debian.datastax.com/community stable main" | tee -a
/etc/apt/sources.list.d/cassandra.sources.list \  
&& curl -L http://debian.datastax.com/debian/repo_key | apt-key add \- \  
&& apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 \--recv 7F0CEB10 \  
&& echo "deb http://repo.mongodb.org/apt/ubuntu "$(lsb_release -sc)"/mongodb-
org/3.0 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-3.0.list \  
&& apt-get update \  
&& apt-get install -y cassandra-tools mongodb-org-shell mongodb-org-tools \  
&& rm -rf /var/lib/apt/lists/* \  
&& curl -O http://stedolan.github.io/jq/download/linux64/jq \  
&& mv jq /usr/bin/jq \  
&& chmod +x /usr/bin/jq  
  
WORKDIR /root  
  
ENTRYPOINT ["/bin/bash"]  

