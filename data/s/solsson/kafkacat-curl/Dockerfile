FROM
solsson/kafkacat@sha256:2c539e4f58960ab7872976ebc664dd92de18cf27e7cbbeb296d654a2351f6ca4  
  
RUN set -ex; \  
export DEBIAN_FRONTEND=noninteractive; \  
runDeps='curl jq'; \  
buildDeps='ca-certificates'; \  
apt-get update && apt-get install -y $runDeps $buildDeps --no-install-
recommends; \  
rm -rf /var/lib/apt/lists/*; \  
\  
apt-get purge -y --auto-remove $buildDeps; \  
rm /var/log/dpkg.log /var/log/apt/*.log

