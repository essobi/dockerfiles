FROM hpess/chef:master  
MAINTAINER Karl Stoney <karl.stoney@hp.com>  
  
# Download Aerospike  
RUN cd /tmp && \  
wget -q -O aerospike.tgz
http://www.aerospike.com/download/server/3.5.9/artifact/el6 && \  
tar -xf aerospike.tgz && \  
rm *.tgz && \  
cd aerospike-server-community-* && \  
yum -y localinstall aerospike-*.x86_64.rpm && \  
rm -rf /tmp/aerospike-*  
  
# Download Aerospike tools  
RUN cd /tmp && \  
wget -q -O aerospike-tools.tgz
http://aerospike.com/download/server/latest/artifact/el6 && \  
tar -xf aerospike-tools.tgz && \  
rm *.tgz && \  
cd aerospike-server-community-* && \  
yum -y localinstall aerospike-tools-*.x86_64.rpm && \  
chown -R docker:docker /opt/aerospike && \  
rm -rf /tmp/aerospike-*  
  
EXPOSE 3000 3001 3002 9918 3003 3004  
ENV HPESS_ENV aerospike  
ENV chef_node_name aerospike.docker.local  
ENV chef_run_list aerospike  
  
COPY services/* /etc/supervisord.d/  
COPY cookbooks/ /chef/cookbooks/  

