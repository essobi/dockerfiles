FROM tecposter/ubuntu:latest  
  
MAINTAINER "zhanjh@126.com"  
  
# ref. https://hub.docker.com/_/mariadb/  
  
#ADD src /usr/local/src  
  
RUN set -ex \  
&& apt-get update \  
&& apt-get upgrade --no-install-recommends --no-install-suggests -y \  
  
&& build_deps="git gcc make build-essential cmake ca-certificates" \  
&& apt-get install -y \--no-install-recommends --no-install-suggests \  
$build_deps \  
  
&& apt-get install -y \--no-install-recommends --no-install-suggests \  
zlib1g-dev libncurses5-dev bison pkg-config libxml2-dev libssl-dev openssl \  
  
# && git config --global http.sslverify false \  
&& cd /usr/local/src \  
&& git clone https://github.com/MariaDB/server.git mariadb \  
&& cd mariadb \  
&& git checkout 10.1 \  
  
&& cmake -DWITH_WSREP=ON -DWITH_INNODB_DISALLOW_WRITES=ON . \  
&& make \  
&& make install \  
  
&& cd / \  
&& rm -rf /usr/local/src/* \  
&& rm -rf /var/lib/apt/lists/* \  
&& apt-get purge -y \--auto-remove $build_deps  

