FROM tecposter/mariadb:latest  
  
MAINTAINER "zhanjh@126.com"  
  
# https://github.com/toughIQ/docker-mariadb-cluster/tree/master/scripts  
  
  
RUN set -ex \  
&& apt-get update \  
&& apt-get upgrade --no-install-recommends --no-install-suggests -y \  
  
&& build_deps="git gcc make build-essential cmake ca-certificates scons" \  
&& apt-get install -y \--no-install-recommends --no-install-suggests \  
$build_deps \  
  
&& apt-get install -y \--no-install-recommends --no-install-suggests \  
rsync libboost-all-dev check lsof \  
  
&& cd /usr/local/src \  
&& git clone https://github.com/MariaDB/galera.git galera \  
&& cd galera \  
&& ./scripts/build.sh \  
&& mkdir /usr/lib64/galera -p \  
&& cp libgalera_smm.so /usr/lib64/galera/ \  
  
&& cd / \  
&& apt-get purge -y \--auto-remove $build_deps \  
&& apt-get autoremove -y \  
&& rm -rf /usr/local/src/* \  
&& rm -rf /var/lib/apt/lists/*  

