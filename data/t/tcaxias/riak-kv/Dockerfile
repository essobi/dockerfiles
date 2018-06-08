# Container for Riak KV configured for Riak CS  
FROM centos:7  
MAINTAINER Tiago Caxias http://github.com/tcaxias  
  
# Pick a RING_SIZE:  
# http://docs.basho.com/riak/kv/latest/setup/planning/cluster-capacity/#ring-
size-number-of-partitions  
# Configure AUTH access with CERT_DIR and PASSWD  
# http://docs.basho.com/riak/kv/latest/using/admin/riak-control/#enabling-ssl-
and-https  
ENV \  
PKGS="pygpgme riak riak-cs python" \  
DEPS="python-pip" \  
REPO="/etc/yum.repos.d/basho.repo" \  
OS="el" \  
DIST="7" \  
RING_SIZE="" \  
PASSWD="" \  
CERT_DIR="" \  
METRICS_PORT="9106" \  
RIAK_KV_DIR="https://packagecloud.io/install/repositories/basho/riak" \  
RIAK_CS_DIR="https://packagecloud.io/install/repositories/basho/riak-cs" \  
UNZIP="python -c \"import
zipfile,sys,StringIO;zipfile.ZipFile(StringIO.StringIO(sys.stdin.read())).extractall(sys.argv[1]
if len(sys.argv) == 2 else '.')\"" \  
RIAK_EXPORTER="https://github.com/anti1869/riak_exporter/archive/master.zip"  
RUN \  
curl "${RIAK_KV_DIR}/config_file.repo?os=${OS}&dist=${DIST}&name=$(hostname)"
>> $REPO && \  
curl "${RIAK_CS_DIR}/config_file.repo?os=${OS}&dist=${DIST}&name=$(hostname)"
>> $REPO && \  
yum install -y $PKGS && \  
yum clean -y all  
  
RUN \  
{ yes | yum install -y epel-release; } && \  
yum install -y $DEPS && \  
pip install supervisor && \  
curl -L $RIAK_EXPORTER | sh -c "$UNZIP /app" && \  
cd /app/riak_exporter-master && \  
python setup.py build install && \  
cd / && rm -rf /app/riak_exporter-master && \  
yum erase -y $DEPS && \  
yum clean -y all  
  
ADD advanced.config /etc/riak/  
ADD supervisord.conf /etc/  
ADD start_riak.sh /app/  
RUN chmod +x /app/*.sh  
  
VOLUME "/var/lib/riak"  
EXPOSE 8087 8098 9106  
CMD [ "supervisord", "-j", "/dev/shm/supervisor.pid", "-t" ]  

