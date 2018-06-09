# MySQL wsrep Dockerfile  
# Solnet Solutions  
# Version: 5.6.23 (5.6:5.6.23-25.10-1trusty)  
  
# Pull base image (Ubunu 14.04)  
FROM ubuntu:14.04  
  
# Build Instructions  
# When building use the following flags:  
# \--tag "solnetcloud/mysql-wsrep:5.6.23"  
  
# Run Instructions:  
# Run a DOC/volume to preserve state of /var/lib/mysql  
# You will probably want to expose the MySQL port (3306) to the host  
# When running use the following flags:  
# \--restart=on-failure  
# The following command line arguments are supported.  
# usage: entry [-h] [--cluster-name [CLUSTER_NAME]] [--rep-user [REP_USER]]  
# [--rep-pass [REP_PASS]] [--root-pass [ROOT_PASS]]  
# [--mon-user [MON_USER]] [--mon-pass [MON_PASS]]  
# [--max-connections [MAX_CONNECTIONS]] [--boot-strap-cluster]  
# rep_addr member_addr [member_addr ...]  
  
# Run a docker container containing a MySQL wsrep Instance  
  
# positional arguments:  
# rep_addr The IP address for this node in cluster  
# member_addr IP address(es) for other member(s) of the cluster  
  
# optional arguments:  
# -h, --help show this help message and exit  
# \--cluster-name [CLUSTER_NAME], -c [CLUSTER_NAME]  
# The MySQL wsrep cluster name, "DBCluster"  
# \--rep-user [REP_USER], -u [REP_USER]  
# The MySQL wsrep replication user, "wsrep_sst-user"  
# \--rep-pass [REP_PASS], -p [REP_PASS]  
# The password for the MySQL wsrep replication user,  
# "changeme"  
# \--root-pass [ROOT_PASS], -P [ROOT_PASS]  
# The password for the MySQL wsrep root user,  
# "changeme2"  
# \--mon-user [MON_USER], -m [MON_USER]  
# The MySQL monitor user, "clustercheckuser"  
# \--mon-pass [MON_PASS], -M [MON_PASS]  
# The password for the MySQL monitor user,  
# "clustercheckpassword"  
# \--max-connections [MAX_CONNECTIONS], -C [MAX_CONNECTIONS]  
# The maximum number of open connections to MySQL, "256"  
# \--boot-strap-cluster, -b  
# Boot strap the cluster, run mysqld with --wsrep-new-  
# cluster  
  
# NOTICE: This is designed to be run as a cluster of 3 MySQL containers
patched for wsrep (Write Set REPlication) each running on separate physical
hosts  
# (to achieve software and hardware redundancy) in active-active
configuration. It is recommended you utilise Weave for this.  
  
# Information  
MAINTAINER Eric Duggan <eric.duggan@solnet.co.nz>  
LABEL Description="This image is used to stand up a MySQL wsrep instance."
Version="5.6.23"  
  
# Patch notes:  
# Version 5.6.23  
# \- Working container running MySQL patched for wsrep  
# \- Added mysqlchk for querying via HAProxy  
# \- Removed mysqlchk (will be in separate container now)  
# \- Give GRANT rights to root user and add monitor user and password  
  
# Set the mysql-wsrep version to be pinned  
ENV MSW_PKG_VRS 5.6.23-25.10-1trusty  
  
# We want to set the uid number and gid number for mysql  
RUN \  
groupadd -g 5000 mysql && \  
useradd -u 5000 -g 5000 -c "MySQL Server,,," -d /nonexistent -s /bin/false
mysql  
  
# Install extra packages  
RUN \  
apt-key adv --keyserver keyserver.ubuntu.com --recv BC19DDBA && \  
echo deb http://releases.galeracluster.com/ubuntu trusty main >>
/etc/apt/sources.list && \  
apt-get update && \  
apt-get install -y python-software-properties python python-jinja2 python-ipy
galera-3 galera-arbitrator-3 mysql-wsrep-5.6 rsync python2.7-mysqldb && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Set timezone  
RUN \  
echo "Pacific/Auckland" > /etc/timezone && \  
dpkg-reconfigure -f noninteractive tzdata  
  
# Remove pre-installed database and create templates directory for wsrep.cnf  
RUN \  
rm -rf /var/lib/mysql/* && \  
mkdir -p /mysql-templates  
  
# Define mountable volumes. We need the database data to be persistant so this
should be mounted as a volume  
VOLUME /var/lib/mysql  
  
# Templates  
COPY templates/my.cnf /mysql-templates/my.cnf  
COPY templates/wsrep.cnf /mysql-templates/wsrep.cnf  
  
# Entry script  
COPY scripts/entry.py /usr/local/bin/entry  
RUN chmod +x /usr/local/bin/entry  
  
# Expose ports to other containers  
# Expose 3306: MySQL  
EXPOSE 3306  
  
# Define the default command as entrypoint  
ENTRYPOINT ["/usr/local/bin/entry"]  

