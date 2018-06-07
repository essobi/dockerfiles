FROM mysql:latest  
  
RUN buildDeps=" \  
wget \  
ca-certificates \  
" \  
&& apt-get update && apt-get install -y $buildDeps --no-install-recommends &&
cd /tmp/ \  
&& wget https://repo.percona.com/apt/percona-release_0.1-4.jessie_all.deb \  
&& dpkg -i percona-release_0.1-4.jessie_all.deb \  
&& apt-get update && apt-get install -y percona-xtrabackup-24 \--no-install-
recommends \  
&& rm -rf /var/lib/apt/lists/* \  
&& apt-get purge -y \--auto-remove -o
APT::AutoRemove::RecommendsImportant=false $buildDeps \  
&& rm -rf /tmp/*  

