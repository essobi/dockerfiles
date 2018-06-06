FROM centurylink/wetty-cli:0.0.8  
  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y wget apt-transport-https  
  
WORKDIR /tmp  
  
RUN wget -nv
https://github.com/coreos/fleet/releases/download/v0.5.0/fleet-v0.5.0-linux-
amd64.tar.gz && \  
tar -xvf fleet-v0.5.0-linux-amd64.tar.gz && \  
mv /tmp/fleet-v0.5.0-linux-amd64/fleetctl /usr/bin/fleetctl && \  
rm -rf /tmp/fleet-v0.5.0-linux-amd64 /tmp/fleet-v0.5.0-linux-amd64.tar.gz  
ENV FLEETCTL_ENDPOINT http://10.1.42.1:4001  
  
RUN wget -nv
https://github.com/coreos/etcd/releases/download/v0.4.5/etcd-v0.4.5-linux-
amd64.tar.gz && \  
tar -xvf etcd-v0.4.5-linux-amd64.tar.gz && \  
mv /tmp/etcd-v0.4.5-linux-amd64/etcdctl /usr/bin/etcdctl && \  
rm -rf /tmp/etcd-v0.4.5-linux-amd64 /tmp/etcd-v0.4.5-linux-amd64.tar.gz  
ENV ETCDCTL_PEERS 10.1.42.1:4001  
  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 \--recv-keys
36A1D7869245C8950F966E92D8576A8BA88D21E9  
RUN echo "deb https://get.docker.io/ubuntu docker main" >
/etc/apt/sources.list.d/docker.list  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y lxc-docker-1.0.1  

