FROM centos:latest  
MAINTAINER Support <support@atomicorp.com>  
  
RUN cd /root && \  
yum -y update && \  
yum -y install wget useradd postfix && \  
NON_INT=1 wget -q -O - https://updates.atomicorp.com/installers/atomic | sh &&
\  
yum -y install ossec-hids-server && \  
yum clean all && \  
rm -rf /var/cache/yum/  
  
RUN curl -Lo /usr/local/bin/kubectl https://storage.googleapis.com/kubernetes-
release/release/v1.9.0/bin/linux/amd64/kubectl && \  
chmod 755 /usr/local/bin/kubectl  
  
ADD default_agent /var/ossec/default_agent  
  
# copy base config  
ADD ossec.conf /var/ossec/etc/  
  
#  
# Initialize the data volume configuration  
#  
ADD data_dirs.env /data_dirs.env  
ADD init.sh /init.sh  
# Sync calls are due to https://github.com/docker/docker/issues/9547  
RUN chmod 755 /init.sh &&\  
sync && /init.sh &&\  
sync && rm /init.sh  
  
#  
# Add the bootstrap script  
#  
ADD entrypoint.sh /entrypoint.sh  
ADD generate-k8s-client-keys.sh /generate-k8s-client-keys.sh  
ADD ossec-remoted.sh /ossec-remoted.sh  
  
#  
# Specify the data volume  
#  
VOLUME ["/var/ossec/data"]  
  
# Expose ports for sharing  
EXPOSE 1514/udp 1515/tcp 514/tcp 514/udp  
  
#  
# Define default command.  
#  
ENTRYPOINT ["/entrypoint.sh"]  

