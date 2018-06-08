# This file creates a container that runs Database (Percona) with Galera
Replication.  
#  
FROM pilchard/centos  
MAINTAINER pilcahrd  
  
ENV PERCONA_VERSION=57  
# Base Deps  
RUN \  
yum install -y http://www.percona.com/downloads/percona-
release/redhat/0.1-4/percona-release-0.1-4.noarch.rpm && \  
yum install -y Percona-XtraDB-Cluster-$PERCONA_VERSION

