#  
# Percona cluster node server  
#  
# Pull base image.  
FROM ubuntu:14.04  
MAINTAINER Konstantinos Christofilos <kostas.christofilos@rocketgraph.com>  
  
# Install base.  
RUN \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y curl vim wget  
  
# Install percona cluster server  
ENV DEBIAN_FRONTEND noninteractive  
RUN echo "deb http://repo.percona.com/apt trusty main" >>
/etc/apt/sources.list.d/percona.list  
RUN echo "deb-src http://repo.percona.com/apt trusty main" >>
/etc/apt/sources.list.d/percona.list  
RUN apt-key adv --keyserver keys.gnupg.net --recv-keys 1C4CBDCDCD2EFD2A  
RUN apt-get update && apt-get -y upgrade  
RUN apt-get install -y percona-xtradb-cluster-56 qpress xtrabackup  
RUN apt-get install -y python-software-properties vim wget curl netcat  
#RUN apt-get install -y percona-xtradb-cluster-56 percona-xtrabackup percona-
toolkit percona-nagios-plugins netcat socat procps  
ENV MYSQL_ROOT_PASSWORD 123456  
ENV MYSQL_PORT 3306  
ENV CLUSTER_NAME percona-cluster  
ENV REP_USER rep  
ENV REP_PASS 123456  
ENV BOOTSTRAP_CLUSTER 0  
#ENV NODE_NAME node-x  
#ENV CLUSTER_IPS  
#ENV CLUSTER_SUBNET  
#ENV NODE_IP  
ADD ./my.cnf /etc/mysql/my.cnf  
  
ADD ./export_env.py /export_env.py  
RUN chmod +x /export_env.py  
  
# Init embedded database  
ADD ./install.sh /install.sh  
RUN chmod +x /install.sh  
RUN /install.sh && rm /install.sh  
  
ADD ./init.sh /mysql-init.sh  
ADD ./run.sh /run.sh  
RUN chmod +x /mysql-init.sh  
RUN chmod +x /run.sh  
  
# Define mountable directories.  
VOLUME ["/var/lib/mysql"]  
  
# Define working directory.  
# WORKDIR /var/lib/mysql  
# Define default command.  
CMD ["/run.sh"]  
  
# Expose ports.  
EXPOSE 3306 4444 4567 4568

