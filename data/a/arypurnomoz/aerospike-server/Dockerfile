FROM debian:latest  
  
ADD http://aerospike.com/download/server/latest/artifact/debian7
/tmp/aerospike.tgz  
  
RUN \  
apt-get update \  
&& apt-get upgrade -y \  
&& apt-get -f install \  
&& apt-get install -y python logrotate wget \  
&& tar zxf /tmp/aerospike.tgz -C /tmp \  
&& dpkg -i /tmp/aerospike*/*.deb \  
&& rm -rf /tmp/aero*  
  
VOLUME ["/opt/aerospike/data"]  
  
# Expose Aerospike ports  
# 3000 – service port, for client connections  
# 3001 – fabric port, for cluster communication  
# 3002 – mesh port, for cluster heartbeat  
# 3003 – info port  
ADD run.sh /tmp/run.sh  
  
EXPOSE 3000 3001 3002 3003  
ENTRYPOINT ["/tmp/run.sh"]  

